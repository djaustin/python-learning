def build_sandwich(*fillings):
    print("Making a sandwich with the following fillings:")
    for filling in fillings:
        print("- " + filling)

build_sandwich('ham', 'cheese', 'mayo')
build_sandwich('chicken', 'hot sauce')
