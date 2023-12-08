# check_users_and_roles.py

from app import User, Role

# Tüm kullanıcıları ve rolleri getir
users = User.query.all()
roles = Role.query.all()

print("Users:")
for user in users:
    print(f"ID: {user.id}, Username: {user.username}, Roles: {[role.name for role in user.roles]}")

print("\nRoles:")
for role in roles:
    print(f"ID: {role.id}, Name: {role.name}")
