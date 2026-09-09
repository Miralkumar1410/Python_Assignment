def fun(s):

    if s.count("@") != 1:
        return False

    username, rest = s.split("@")

    if rest.count(".") != 1:
        return False

    website, extension = rest.split(".")

    if not username.replace("-", "").replace("_", "").isalnum():
        return False

    if not website.isalnum():
        return False

    if not extension.isalpha():
        return False

    if len(extension) > 3:
        return False

    return True


def filter_mail(emails):
    return list(filter(fun, emails))