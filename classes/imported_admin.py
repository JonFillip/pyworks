# 9-11. Imported Admin
from classes.privilege_admin import *

admin_user = Admin("jake", "dean", 22, "kiev", "QA engineer")
admin_user.describe_user()
admin_user.privilege.show_privileges()
