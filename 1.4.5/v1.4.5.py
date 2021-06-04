#encoding:utf-8

import tkinter as tk
import tkinter.font as tkFont
import random
import webbrowser
import tkinter.messagebox
import platform

window = tk.Tk()
window.title('生成器')
#字体
ans=' '
f1 = tkFont.Font(size=20, weight=tkFont.BOLD)
f2 = tkFont.Font(size=13, weight=tkFont.BOLD)
f3 = tkFont.Font(size=12)
f4 = tkFont.Font(size=12, weight=tkFont.BOLD)
f5 = tkFont.Font(size=11)
v = tk.IntVar()
v.set(1)
c = tk.IntVar()
c.set(1)
n=' '
version='v1.4.5'
system=platform.platform()
sys=system[0:10];

if sys == 'Windows-10':
    sys = 'Windows 10'
elif sys[0:5] == 'MacOS' | sys[0:5] == 'macOS':
    sys = 'MacOS'

#左侧字
tk.Label(window, text="营销号生成器",font=f1).grid(row=0,column=0,columnspan=4)
tk.Label(window, text="主体：").grid(row=1,column=0)
tk.Label(window, text="事件：").grid(row=2,column=0)
tk.Label(window, text="说法：").grid(row=3,column=0)
tk.Label(window, text=version).grid(row=9,column=0,columnspan=2,sticky="w")
#tk.Label(window, text="——Made by Anderson_Yang      ").grid(row=9,column=2,columnspan=2,sticky="e")
#输入框
e1 = tk.Entry(window,width=12)
e2 = tk.Entry(window,width=12)
e3 = tk.Entry(window,width=12)
e1.grid(row=1, column=1)
e2.grid(row=2, column=1)
e3.grid(row=3, column=1)
#检测复选框
check = tk.BooleanVar()
#打开网页
def web1():
    webbrowser.open("https://andersonyang.icoc.me/")
def web2():
    webbrowser.open("https://github.com/Github-Anderson/yxh-maker")
#当生成被点击
def show():
    #读取
    t1.delete(0.0,tk.END)
    t2.delete(0.0,tk.END)
    a = e1.get()
    b = e2.get()
    c = e3.get()
    if len(a)==0:
        tkinter.messagebox.showwarning('出错了','主体不能为空！')
        t1.insert('end','标题会显示在这里～')
        t2.insert('end','内容会显示在这里～')
    elif len(b)==0:
        tkinter.messagebox.showwarning('出错了','事件不能为空！')
        t1.insert('end','标题会显示在这里～')
        t2.insert('end','内容会显示在这里～')
    elif len(c)==0:
        tkinter.messagebox.showwarning('出错了','说法不能为空！')
        t1.insert('end','标题会显示在这里～')
        t2.insert('end','内容会显示在这里～')
    else:
        i=random.randint(1,9)
        if i==1:
            title = '你听说过'+a+b+'吗？不知道就丢脸了！'
        if i==2:
            title = '原来'+a+b+'，看完跪了。。。'
        if i==3:
            title = a+'竟然'+b+'！这到底是怎么一回事？'
        if i==4:
            title = a+'为何'+b+'？原来他早已告诉我们答案！'
        if i==5:
            title = a+b+'意外走红，网友：我居然不知道！'
        if i==6:
            title = '为什么'+a+b+'？专家给出答案！'
        if i==7:
            title = '火遍全网的'+a+'究竟是什么梗？'
        if i==8:
            title = '如何看待'+a+b+'?'
        if i==9:
            title = '专家不会告诉你的秘密：'+a+'为什么'+b+'?'
        if v.get()==1:
            ans = '       ' + a + b +'是怎么回事呢？' + a + '相信大家都很熟悉，但是' + a + b + '是怎么回事呢，下面就让小编带大家一起了解吧。\n' + '       ' + a + b + '，其实就是' + c + '，大家可能会很惊讶' + a + '怎么会' + b + '呢？但事实就是这样，小编也感到非常惊讶。\n'+'       '+'这就是关于' + a + b + '的事情了，大家有什么想法呢，欢迎在评论区告诉小编一起讨论哦！'
        if v.get()==2:
            ans = '       世界之大无奇不有，小编带你看世界，Hello大家好我是XX看世界。近日，韩国有一外国小哥突发奇想，他认为'+a+b+'，那么什么是'+a+'呢？众所周知'+a+b+'本质上就是'+c+'，但是这小哥把它玩出了什么玩法呢？事实上他居然认为'+a+b+'，大家可能会很惊讶' + a + '怎么会' + b + '呢？但事实就是这样，小编也感到非常惊讶。'+'好了本期节目就到这里了，喜欢的小伙伴可以点一下关注，欢迎在评论区告诉小编一起讨论哦！'
        t1.insert('end',title)
        t2.insert('end',ans)
#当清空被点击
def clear():
    t1.delete(0.0,tk.END)
    t1.insert('end','标题会显示在这里～')
    t2.delete(0.0,tk.END)
    t2.insert('end','内容会显示在这里～')
    e1.delete(0,tk.END)
    e2.delete(0,tk.END)
    e3.delete(0,tk.END)

def info1():
    info = tk.Toplevel(window)
    info.title('生成器')
    tk.Label(info, text="版本信息",font=f1).grid(row=0,column=1,columnspan=3)
    i1=tk.Label(info)
    # i1.image = tk.PhotoImage(file='1.png')
    # i1['image']=i1.image
    i1.grid(row=0,column=0,rowspan=4)
    tk.Label(info,text="作者:Anderson_Yang").grid(row=1,column=1,columnspan=2,sticky="w")
    tk.Label(info,text="版本:"+version+'('+sys+')').grid(row=2,column=1,columnspan=2,sticky="w")
    tk.Label(info,text="主页:https://andersonyang.icoc.me/").grid(row=3,column=1,columnspan=2,sticky="w")
    tk.Label(info,text="此程序已在GitHub开源                    ",font=f4).grid(row=4,column=1,columnspan=2,sticky="w")
    tk.Label(info,text="Copyright © 2019-2020.",font=f5).grid(row=5,column=1,columnspan=2)
    tk.Button(info, text="主页", width=8, command=web1).grid(row=4, column=0)
    tk.Button(info, text="关闭", width=8, command=info.destroy).grid(row=5, column=0)
    tk.Button(info, text="前往", width=8, command=web2).grid(row=4, column=2,sticky="e")
    
    #tk.messagebox.showinfo(title='帮助', message='作者:Anderson_Yang\n版本信息:'+version+'\n主页:https://andersonyang.icoc.me')

def help1():
    e1.delete(0,tk.END)
    e2.delete(0,tk.END)
    e3.delete(0,tk.END)
    e1.insert(0,'营销号生成器')
    e2.insert(0,'用不了')
    e3.insert(0,'这都不会用')
    show()
    '''
    h1 = tk.Toplevel(window)
    h1.title('生成器')
    tk.Label(h1, text="帮助",font=f1).grid(row=0,column=0)
    t1 = tk.Text(h1,width=30,height=9,font=f3)
    t1.grid(row=1,column=0)
    t1.insert('end','')
    '''

def up1():
    tkinter.messagebox.showinfo('检查更新','已经是最新版本了！('+version+')')

def im1():
    def bc1():
        name1=en1.get()
        ans1=t1.get('0.1','end')+t2.get('0.1','end')
        an1 = open(name1+'.txt',mode='w')
        an1.write(ans1)
        an1.close()
        im.destroy()
    
    im = tk.Toplevel(window)
    im.title('生成器')
    tk.Label(im, text="导出",font=f1).grid(row=0,column=0,columnspan=3)
    tk.Label(im,text="名称:").grid(row=1,column=0)
    en1 = tk.Entry(im,width=12,justify='right')
    en1.grid(row=1, column=1)
    tk.Label(im,text=".txt").grid(row=1,column=2)
    #la1=tk.Label(im,text="路径:").grid(row=1,column=0)
    #en2 = tk.Entry(im,width=16)
    #en2.grid(row=1, column=1)
    c1 = tk.Checkbutton(im,text="默认路径",variable=c,onvalue=1,offvalue=0,state="disabled").grid(row=2, column=1)
    tk.Button(im,text="保存", width=7,command=bc1).grid(row=3, column=1,columnspan=2,sticky="w")
    tk.Button(im,text="关闭", width=7,command=im.destroy).grid(row=3, column=1,columnspan=2,sticky="e")

#按钮
tk.Button(window, text="生成", width=9, command=show).grid(row=5, column=0, columnspan=2,sticky="w")
tk.Button(window, text="导出", width=9, command=im1).grid(row=5, column=0, columnspan=2,sticky="e")
tk.Button(window, text="清空", width=9, command=clear).grid(row=6, column=0, columnspan=2,sticky="w")
tk.Button(window, text="退出", width=9, command=window.quit).grid(row=6, column=0, columnspan=2,sticky="e")
#帮助按钮
tk.Button(window, text="帮助", width=9, command=help1).grid(row=9, column=3,sticky='w')
tk.Button(window, text="版本信息", width=9, command=info1).grid(row=9, column=3,sticky="e")
#结果框
t1 = tk.Text(window,width=28,height=1,font=f2)
t1.grid(row=1,column=2,columnspan=2,sticky=tk.E+tk.W)
t1.insert('end','标题会显示在这里～')
t2 = tk.Text(window,width=32,height=8,font=f3)
t2.grid(row=2,column=2,rowspan=6,columnspan=2,sticky=tk.E+tk.W)
t2.insert('end','内容会显示在这里～')
#单选框
tk.Radiobutton(window,text='文章',variable=v,value=1).grid(row=4,column=0)
tk.Radiobutton(window,text='视频配音',variable=v,value=2).grid(row=4,columnspan=2,sticky="e")
#功能快捷键


m1 = tk.Menu(window)
window.config(menu=m1)
mb1 = tk.Menu(m1,tearoff=0)
mb1.add_command(label="导出",command=im1,accelerator='Command-S')
mb1.add_command(label="帮助",command=help1)
mb1.add_separator()
mb1.add_command(label="检查更新",command=up1)
mb1.add_command(label="版本信息",command=info1)
m1.add_cascade(label="文件", menu=mb1)

window.config(menu=m1)
mb2 = tk.Menu(m1,tearoff=0)
mb2.add_command(label="生成",command=show,accelerator='Command-T')
mb2.add_command(label="清空",command=clear,accelerator='Command-R')
mb2.add_command(label="关闭",command=window.quit,accelerator='Command-Q')
m1.add_cascade(label="操作", menu=mb2)

window.mainloop()