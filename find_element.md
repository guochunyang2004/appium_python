# find_element


# 通过ID定位目标元素
driver.find_element_by_id('i1')
 
# 通过className定位目标元素
driver.find_element_by_class_name('c1')
 
# 通过name属性定位目标元素
driver.find_element_by_name('n1')
 
# 通过Xpath定位目标元素
driver.find_element_by_xpath('//*[@id="i1"]').send_keys('这是在输入框内输入的文本信息')
 
# 通过css Selector定位目标元素
element=driver.find_element_by_css_selector('input[placeholder="请通过CSS SELECTOR定位元素"]')
element.send_keys('111')
 
# 通过标签名称定位(注：在一个页面中，标签一定会重复，所以不用这个来进行定位)
# 默认写在多个相同标签的第一个里面
driver.find_element_by_tag_name('input').send_keys('111')
 
# 通过标签中的文本查找元素
driver.find_element_by_link_text('跳转大师兄博客地址').click()
 
# 通过标签中文本的模糊匹配查找
driver.find_element_by_partial_link_text('大师兄').click()

# 单数的父类，是上面8种单数方式的底层封装。参数化的一种调用方式而已。
driver.find_element()


# 获取复数形式
elements = driver.find_elements_by_css_selector('select')