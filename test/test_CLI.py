import json
import os
import pytest
from datetime import datetime
from src.mainCLi import process

time_format = "%m/%d/%Y, %H:%M:%S"

def tasks_get():
    with open("tasks_list.json", "r") as tasks_list:
         return json.load(tasks_list)

def test_add():
    process(['add', 'wake up'])
    process(['add', 'have breakfast'])
    process(['add', 'work'])
    assert len(tasks_get()) == 3

def test_update():
    process(['update', '3', 'walk'])
    tasks = tasks_get()
    assert tasks['3']['description'] == 'walk'
    assert tasks['3']['updated_at'] == datetime.now().strftime(time_format)
    with pytest.raises(KeyError):
        process(['update', '4', 'sleep'])

def test_delete():
    process(['delete', '3'])
    assert len(tasks_get()) == 2
    with pytest.raises(KeyError):
        process(['delete', '5'])

def test_mark_done():
    process(['mark-done', '2'])
    assert tasks_get()['2']['status'] == 'done'
    with pytest.raises(KeyError):
        process(['mark-done', '5'])

def test_mark_in_progress():
    process(['mark-in-progress', '1'])
    assert tasks_get()['1']['status'] == 'in-progress'
    with pytest.raises(KeyError):
        process(['mark-in-progress', '5'])

def test_clear():
    if os.path.exists("tasks_list.json"):
        os.remove("tasks_list.json")

