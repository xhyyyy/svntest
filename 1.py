
def threeindex(i,dir1,dir2,dir3,pr):
    while i:
        print(r"路径为{0}\{1}\{2},权限为{3}".format(dir1, dir2, dir3, pr))
        if pr == "rw" or pr== "r":
            pr = "r"
            i = i - 1
        else:
            break

        if i == 2:
            print(r"路径为{0}\{1},权限为{2}".format(dir1, dir2, pr))
            pr = "r"
            i = i - 1
        if i == 1:
            print(r"路径为{0},权限为{1}".format(dir1, pr))
            i = i - 1

def fourindex(i,dir1,dir2,dir3,dir4,pr):
    while i:
        print(r"路径为{0}\{1}\{2}\{3},权限为{4}".format(dir1, dir2, dir3,dir4,pr))
        if pr == "rw" or pr == "r":
            pr = "r"
            i = i - 1
        else:
            break
        if i == 3:
            print(r"路径为{0}\{1}\{2},权限为{3}".format(dir1, dir2, dir3, pr))
            i = i -1
        if i == 2:
            print(r"路径为{0}\{1},权限为{2}".format(dir1, dir2, pr))
            pr = "r"
            i = i - 1
        if i == 1:
            print(r"路径为{0},权限为{1}".format(dir1, pr))
            i = i - 1








pr = "rw"
i =4
dir1 = "c:"
dir2 = "new"
dir3 = "new2"
dir4 = "new3"
fourindex(i,dir1,dir2,dir3,dir4,pr)


