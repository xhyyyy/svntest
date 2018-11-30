class ModelTree():
    def __init__(self,name,quanxian = None):
        self.name = name
        #初始当前节点的名字
        self.quanxian =quanxian
        #初始化父节点的权限，默认为none
        self.child = {}
        #初始化下一级子节点

    def get_child(self,name,quanxian = None):
        return self.child.get(name,quanxian)
    #获取子节点的名字，没有就返回none 初始化子节点的权限

    def add_child(self,name,obj=None):
        if obj and not isinstance(obj,ModelTree):
            raise ValueError('TreeNode only add another TreeNode obj as child')
        #判断obj是不是类里面的对象
        if obj is None:
            obj = TreeNode(name)
        obj.quanxian=self
        obj.child




