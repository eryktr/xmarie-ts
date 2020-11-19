import pytest

def test_run(xmarie_driver):
    xmarie_driver.toggle_breakpoints([4])
    xmarie_driver.click_run_btn()
    assert xmarie_driver.get_label_text('AC') == "0 (0x0)"
    assert xmarie_driver.get_label_text('PC') == "6 (0x6)"
    assert xmarie_driver.get_label_text('X') == "0 (0x0)"
    assert xmarie_driver.get_label_text('Y') == "0 (0x0)"


def test_debug(xmarie_driver):
    import time
    xmarie_driver.replace_code_with([
        'Load X', 
        'Add Y', 
        'Add Z', 
        'Halt',
        'X, DEC 1',
        'Y, DEC 2',
        'Z, DEC 3',
    ])
    xmarie_driver.toggle_breakpoints([1, 2, 4])
    xmarie_driver.click_debug_btn()
    