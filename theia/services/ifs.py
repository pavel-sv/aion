class Columns:

    def __init__(self):
        super().__init__()
        self.__columns = {
            'CO': {
                'pre-sellected': [
                    'Order No',
                    'Sales Part No',
                    'Sales Qty',
                    'Customer No',
                    'Promised Delivery Date/Time',
                    'Price/Curr',
                    'Sales Part Description',
                    'Last Actual Ship Date',
                    'Planned Ship Date/Time',
                    'Supply Code',
                    'Status',
                    'Order Type',
                    'Customer Name',
                    'Coordinator',
                    'Site',
                    'Configurable',
                    'Configuration ID',
                    'Gross Amt/Curr',
                    'Wanted Delivery Date/Time',
                    'Sales Part Type',
                    'Part No',
                    'Purchase Part No',
                    'Supplier',
                    'Supply Site',
                    'Cust Stat Grp',
                    'SalesGroup',
                    'Currency',
                    'Currency Rate',
                    'Price Source',
                    'Price/Base',
                    'Source Price/Curr',
                    'Price incl Tax/Base',
                    'Sales Price incl Tax/Curr',
                    'Net Amt/Base',
                    'Gross Amt/Base',
                    'Net Amount/Curr',
                    'Cost',
                    'Total Cost/Base',
                    'Target Date/Time',
                    'Planned Delivery Date/Time',
                    'Planned Due Date',
                    'First Actual Ship Date',
                    'Created',
                    'Tax Liability',
                    'Tax Code',
                    'Tax Amount/Base',
                    'Discount (%)',
                    'Group Discount (%)',
                    'Additional Discount (%)',
                    'Total Order Line Discount (%)',
                    'Delivery Type',
                    'Demand Code',
                    'Order Ref 1',
                    'Customer Warranty',
                    'Delivery Terms',
                    'Del Terms Location',
                    'Ship Via Code',
                    'Confirmed Date',
                    'Region Code',
                    'Program ID',
                    'Project ID',
                    'Project Name',
                    'Sub Project ID',
                    'Sub Project Description',
                    'Activity ID',
                    'Activity Description',
                    'Activity Sequence',
                    'Cost Cent',
                    'BusinessLi',
                    'Counterpar',
                    'Project',
                    'Shopord',
                    'Ext CO No',
                    'Ext CO Site',
                    'Eur Value',
                    'Country of Origin',
                    'Financial Project',
                    'Price Incl Discount',
                    'Total Cost Eur',
                    'Customs Stat No'
                ],
                'categorical': [
                    'Supply Code',
                    'Status',
                    'Order Type',
                    'Coordinator',
                    'Site',
                    'Sales Part Type',
                    'Supplier',
                    'Cust Stat Grp',
                    'Currency',
                    'Delivery Type',
                    'Demand Code',
                    'Customer Warranty',
                    'Delivery Terms',
                    'Region Code',
                    'BusinessLi',
                    'Country of Origin'
                ],
                'datetimes': [
                    'Created'
                ],
                'integer': [
                    'Customs Stat No',
                    'Activity Sequence',
                    'Group Discount (%)',
                    'Discount (%)',
                    'Cost Cent'
                ],
                'float': [
                    'Price/Curr',
                    'Gross Amt/Curr',
                    'Currency Rate',
                    'Price/Base',
                    'Price incl Tax/Base',
                    'Net Amt/Base',
                    'Gross Amt/Base',
                    'Net Amount/Curr',
                    'Cost',
                    'Total Cost/Base',
                    'Eur Value',
                    'Price Incl Discount',
                    'Total Cost Eur'
                ],
                'year_month': [
                    'Month',
                    'Year'
                ]
            }
        }

    @property
    def columns(self):
        return self.__columns


class SalesPart:

    def __init__(self):
        super().__init__()
