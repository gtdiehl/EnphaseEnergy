from envoy_utils.passwordCalc import emupwGetMobilePasswd


class EnvoyUtils:
    def __init__():
        pass

    def get_password(serial_num, user_name):
        return emupwGetMobilePasswd(str.encode(serial_num), str.encode(user_name))
