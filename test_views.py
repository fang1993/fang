# class A(object):
#     a=1
#
#     def fun1(self):
#         print('foo')
#     @classmethod
#     def fun2(cls):
#         print('foo2')
#         print(A.a)
#         cls().fun1()
# A.fun2()
from functools import partial
import requests
from log_tool.log_simple_util import get_logger, get_request_logger
from rest_framework.test import APITestCase
from rest_framework import status

COOKIES = '''xxxx'''
log_root_path = "xxx"
is_debug = True if dsp_is_debug == '1' else False
get_logger = partial(get_logger, log_path=log_root_path, is_debug=is_debug, is_write_file=True)


class Workflow_tests(APITestCase):
    @classmethod
    def setUp(self):
        self.client = requests.session()
        self.client.headers.update({'Content-Type': 'application/json'})
        self.client.headers.update({'Cookie': COOKIES.strip()})
        self.workflow_url = "http://127.0.0.1:9000/workflow/"
        self.uuid = 'xxx'
        self.runid = 'xx'
        self.logger = get_logger('workflow')
        self.logger.debug('开始初始化')

        Experiment.objects.create(
            experiment_name='xx', experiment_type='4', remake='xxx', project_id='1', user_id='1'
        )
        Template.objects.create(
            description='template-test',
            tag=0,
            env='test',
            workflow_content=json.dumps({
                'nodes': [],
                'edges': [],
                'props': {
                    'uuid': 'xxx',
                    'etype': 'standalone'
                }
            })
        )

    def tearDown(self):
        self.logger.debug('开始测试')

    def test_psst_workflow(self):
        url = self.workflow_url
        self.logger.debug(f'当前测试路径为{url}')
        data = {'xx'}
        self.logger.debug(f'当前请求参数为{data}')
        response = self.client.post(
            url, data=json.dumps(data)
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('message'), '请求成功')

    def test_put_workflow_content(self):


    def test_get_all_workflow(self):
        url = self.workflow_url + 'list'
        self.logger.debug(f'当前测试路径为{url}')
        params = {'project_id': '1', 'env': 'test'}
        response = self.client.get(url, params=params)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('message'), '请求成功')
        self.logger.debug(response.json().get('result'))
