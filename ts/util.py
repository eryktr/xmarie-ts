def to_register_label_format(dec, hex_):
    return f'{dec} ({hex_})'


def assert_register_labels_content(driver, **kwargs):
    for regname, value in kwargs.items():
        print(regname)
        assert driver.get_label_text(regname) == value
