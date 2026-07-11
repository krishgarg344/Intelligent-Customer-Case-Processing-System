# department mapping logic

DEPARTMENT_MAP = {
    'Billing': 'Finance & Billing',
    'Technical': 'Technical Support',
    'Shipping': 'Logistics',
    'Account': 'Account Services',
    'General': 'General Support',
}
DEFAULT_DEPARTMENT = 'General Support'


def assign_department(category):
    return DEPARTMENT_MAP.get(category, DEFAULT_DEPARTMENT)