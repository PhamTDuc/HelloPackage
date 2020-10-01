# from hello_package import hello_package # Failed
import hello_package  # Success
from package import module  # Success
module.hello_module()
hello_package.hello()
