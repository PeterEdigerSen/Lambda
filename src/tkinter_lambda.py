import tkinter as tk
import functools as ft


def f1(event=None):
    print('f1')


def f2(p, event=None):
    print('f2', p)


root = tk.Tk()
root.geometry('200x200+500+500')

tk.Button(root, text='B 1', command=f1).pack()
tk.Button(root, text='B 2', command=ft.partial(f1)).pack()
tk.Button(root, text='B 3', command=lambda: f1()).pack()
tk.Button(root, text='B 4', command=lambda: print('f1')).pack()

tk.Button(root, text='B 5', command=ft.partial(f2, 5)).pack()
tk.Button(root, text='B 6', command=lambda: f2(5)).pack()
tk.Button(root, text='B 7', command=lambda: print('f2', 5)).pack()

root.bind('a', f1)
root.bind('b', ft.partial(f1))
root.bind('c', lambda e: f1())
root.bind('d', lambda e: print('f1'))

root.bind('e', ft.partial(f2, 7))
root.bind('f', lambda e: f2(7))
root.bind('g', lambda e: print('f2', 7))

root.mainloop()
