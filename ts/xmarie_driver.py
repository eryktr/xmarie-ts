import os
from selenium.webdriver.common.keys import Keys

XMARIE_INDEX_URI = os.getenv('XMARIE_INDEX_URI')

class XmarieDriver:
    def __init__(self, driver):
        self.driver = driver
        driver.get(XMARIE_INDEX_URI)

    def get_label_text(self, labelid):
        return self.find_element_by_id(labelid).text

    def _locate_line_in_editor(self, num):
        lines = self.driver.find_elements_by_class_name('CodeMirror-linenumber')
        for l in lines:
            if l.text == str(num):
                return l

    def toggle_breakpoints(self, line_numbers):
        for lineno in line_numbers:
            self._locate_line_in_editor(lineno).click()

    def click_run_btn(self):
        self.find_element_by_id('runBtn').click()    

    def click_debug_btn(self):
        self.find_element_by_id('debugBtn').click()

    def click_continue_btn(self):
        self.find_element_by_id('continueBtn').click()

    def click_step_btn(self):
        self.find_element_by_id('stepBtn').click()

    def click_profile_btn(self):
        self.find_element_by_id('profileBtn').click()

    def replace_code_with(self, lines):
        codemirror = self.find_element_by_id('codemirror')
        line = codemirror.find_element_by_class_name('CodeMirror-line')
        line.click()
        textarea = codemirror.find_element_by_css_selector('textarea')
        textarea.send_keys(Keys.CONTROL + 'a')
        textarea.send_keys(Keys.DELETE)
        for line in lines:
            textarea.send_keys(f'{line}\n')

    def set_input(self, lines):
        input_area = self.find_element_by_id('inputArea')
        input_area.click()
        input_area.send_keys('\n'.join(lines))

    def get_output_lines(self):
        return self.find_element_by_id('output').text.split('\n')

    def __getattr__(self, *a, **kw):            
        return getattr(self.driver, *a, **kw)