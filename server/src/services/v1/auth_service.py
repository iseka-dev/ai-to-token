from schemas.v1.auth_schemas import LoginSchema


class AuthService:
    async def login(self, data: LoginSchema):
        user = await users_repo.get_by_eth_account(data.eth_address)
        # if pwd_context.verify(data.password, user.password):
        #     user_permissions = await RolePermissionsService().get_role_permissions(user.role_id)
        #     permission_names = [permission["name"] for permission in user_permissions]
        #     user_data = dict(user._mapping)
        #     user_data["permissions"] = permission_names
        #     user_data["exp"] = datetime.utcnow() + timedelta(minutes=settings.JWT_TTL)
        #     user_data["type"] = TokenTypes.AUTH
        #     payload = self._build_token_payload(user_data)
        #     token = auth_helper.create_token(payload)
        #     refresh_ttl = datetime.utcnow() + timedelta(minutes=settings.JWT_REFRESH_TTL)
        #     payload["exp"] = refresh_ttl
        #     payload["type"] = TokenTypes.REFRESH
        #     refresh_token = auth_helper.create_token(payload)
        #     return {"token": token, "refresh_token": refresh_token}
        # raise InvalidCredentialsException("Invalid credentials, please try again.")
    pass
