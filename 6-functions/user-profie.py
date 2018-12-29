def build_profile(first_name, last_name, **attributes):
    profile = {}
    profile['first_name'] = first_name
    profile['last_name'] = last_name
    for key, value in attributes.items():
        profile[key] = value
    return profile

print(build_profile('dan', 'austin', title='mr', job='DevOps Engineer'))
