import os

from . import forms
from . import utils
from . import data

from django.conf import settings
from django.core.files.storage import default_storage


class UIEventHandler:

    FILE_DIR = settings.FILES_STORAGE

    def __init__(self):
        super().__init__()
        self._command = {
            'view': {
                'upload': self.__set_file_upload_view,
                'files': self.__set_listfiles_view,
                'delete': self.__set_delete_files_view
            },
            'action': {
                'delete': self.__delete_sellected_files,
                'format': self.__format_sellected_file
            }
        }
        self._data_handler = data.DataHandler()
        self.__view_context = dict()

    def request_handler(self, request):
        self.__check_file_dir()
        self.__check_is_file_upload(request)
        if request.POST.__contains__('view-btn'):
            try:
                self.__on_click['view'][request.POST.get('view-btn')]()
            except KeyError as e:
                print(f"This option {e} was not found")
        elif request.POST.__contains__('action-btn'):
            try:
                self.__on_click[
                    'action'][request.POST.get('action-btn')](request)
            except KeyError as e:
                print(f"This option {e} was not found")

    @property
    def __on_click(self):
        return self._command

    @property
    def view_context(self):
        return self.__view_context

    @view_context.setter
    def set_template_context(self, value):
        self.__view_context = value

    def __check_file_dir(self):
        if os.listdir(self.FILE_DIR):
            self.view_context['file_dir_not_empty'] = True
        else:
            self.view_context['file_dir_not_empty'] = False

    def __check_is_file_upload(self, request):
        form = forms.UploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data['upload']
            file_path = utils.return_file_path(file.name, self.FILE_DIR)
            default_storage.save(file_path, file)
            self.view_context['file_dir_not_empty'] = True

    def __set_file_upload_view(self):
        form = forms.UploadForm()
        self.view_context['form'] = form
        self.view_context['view'] = 'view_uploda_file'

    def __set_listfiles_view(self):
        self.view_context['view'] = 'view_uploaded_files'
        self.view_context['files'] = os.listdir(self.FILE_DIR)
        self.view_context['form'] = forms.FileClassForm()

    def __set_delete_files_view(self):
        self.view_context['files'] = os.listdir(self.FILE_DIR)
        self.view_context['view'] = 'view_delete_files'

    def __delete_sellected_files(self, request):
        items = request.POST.getlist('on_delete')
        for item in items:
            file_path = os.path.join(self.FILE_DIR, item)
            os.remove(file_path)
            self.__check_file_dir()
            self.__set_delete_files_view()

    def __format_sellected_file(self, request):
        form = forms.FileClassForm(request.POST)
        if form.is_valid():
            self._data_handler.data_handler_set_properties(
                form.cleaned_data['option'],
                os.path.join(self.FILE_DIR, request.POST.get('sellected'))
            )
            self._data_handler.execute[request.POST.get('action-btn')]()
            print(list(self._data_handler.formated_data.keys()))
