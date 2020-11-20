import pytest
from ts.util import to_register_label_format, assert_register_labels_content

def test_run(xmarie_driver):
    xmarie_driver.toggle_breakpoints([4])
    xmarie_driver.click_run_btn()
    assert_register_labels_content(
        xmarie_driver,
        AC=to_register_label_format('0', '0x0'),
        PC=to_register_label_format('6', '0x6'),
        X=to_register_label_format('0', '0x0'),
        Y=to_register_label_format('0', '0x0'),
    )


def test_debug(xmarie_driver):
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
    assert_register_labels_content(
        xmarie_driver,
        AC=to_register_label_format('0', '0x0'),
    )
    xmarie_driver.click_continue_btn()
    assert_register_labels_content(
        xmarie_driver,
        AC=to_register_label_format('1', '0x1'),
    )
    xmarie_driver.click_step_btn()
    assert_register_labels_content(
        xmarie_driver,
        AC=to_register_label_format('3', '0x3'),
    )
    xmarie_driver.click_continue_btn()
    assert_register_labels_content(
        xmarie_driver,
        AC=to_register_label_format('6', '0x6'),
    )