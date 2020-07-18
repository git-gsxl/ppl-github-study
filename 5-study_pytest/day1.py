'''
pytest是一个非常成熟的全功能的Python测试框架，适合从简单的单元到复杂的功能测试，主要特点有以下几点：

1. 简单灵活，容易上手；

2. 支持参数化；

3. 能够支持简单的单元测试；

4. 标记测试功能与属性

5. 复杂的功能测试，比如可以做selenium等自动化测试、接口自动化测试（pytest+requests）;

6. pytest具有很多第三方插件，并且可以自定义扩展，比较好用的如pytest-selenium（集成selenium）、pytest-study_html（完美html测试报告生成）、pytest-rerunfailures（失败case重复执行）等；

7. Skip和xfail：处理不成功的测试用例；

8. 可以很好的和jenkins集成；

9. 通过xdist插件分发测试到多个CPU

'''

# 文件名以test_*.py 或 *_test.py
# 类已 Test 开头
# 函数以 test_* 开头
'''
参数：
1.显示打印信息：pytest -s              （加 \n 分行）
2.显示详细信息：pytest -v
3.简洁显示信息：pytest -q
4.运行指定用例：pytest -k case_name     (case_name可类可函数，模糊匹配)
5.运行类用例且不运行类某个用例：pytest -v -k "Test_api1 and not test_a"
6.失败停止测试：pytest -x
7.指定个数失败后停止测试：pytest --maxfail=2
8.运行上一次失败用例（或没失败的）：pytest --last-failed
'''

# fixture 自己定义用例前后置




