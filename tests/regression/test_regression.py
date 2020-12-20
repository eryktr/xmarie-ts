import pytest
from ts.util import to_register_label_format, assert_register_labels_content

def test_run(xmarie_driver):
    xmarie_driver.toggle_breakpoints([4])
    xmarie_driver.set_input(['0xA'])
    xmarie_driver.click_run_btn()

    assert_register_labels_content(
        xmarie_driver,
        AC=to_register_label_format('55', '0x37'),
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

def test_sum(xmarie_driver):
    xmarie_driver.replace_code_with([
        'Loop, Load X',
        'Store X_STORE',
        'Load SUM',
        'Add X_STORE',
        'Store SUM',
        'Load X_STORE',
        'Add NEG_ONE',
        'Store X',
        'Skipcond 400',
        'Jump Loop',
        'Halt',
        'X, DEC 10',
        'X_STORE, DEC 0',
        'SUM, DEC 0',
        'NEG_ONE, HEX 0xFFFFF',
    ])
    xmarie_driver.click_run_btn()
    variables = xmarie_driver.find_element_by_id('variables')
    assert "SUM: 55" in variables.text
    assert "X: 0" in variables.text


@pytest.mark.parametrize('func', [
    'click_debug_btn',
    'click_run_btn',
    'click_profile_btn',
])
def test_input_in_debug_run_and_profile(xmarie_driver, func):
    xmarie_driver.set_input(['0x12345'])
    xmarie_driver.replace_code_with([
        'Input',
        'Output',
        'Halt',
    ])
    getattr(xmarie_driver, func)()

    assert xmarie_driver.get_output_lines() == [
        '0x12345'
    ]
