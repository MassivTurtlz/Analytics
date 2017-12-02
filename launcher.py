import SQL_COMMON_HELPERS
import GetData

#table to create
target = ['mainframes']


print()
print(SQL_COMMON_HELPERS.engineStart(target))
print(GetData.exampleQuery(target))