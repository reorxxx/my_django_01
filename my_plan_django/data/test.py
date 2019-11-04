import data

def test_create_task():
    data.create_task("测试任务", "用来测试的", "", "2019-11-20 00:00", "2019-11-21 00:00")

def test_update_task():
    title = "title"
    describe = "t_describe"
    content = "t_content"
    start_time = "t_start_time"
    end_time = "t_end_time"
    need_message = "need_message"
    need_repeat = "need_repeat"

    data.update_task("2019102518293432135",{title: "修改后的titie", describe: "修改后的描述", content: "修改后的内容", start_time: "2019-10-01 00:00",end_time: "2020-01-01 00:00", need_message: 9, need_repeat: 9})


def test_get_task_list():
    tasks = data.get_task_list(5, 0)
    for x in tasks:
        print(x)
    print("----")
    tasks = data.get_task_list(5, 1)
    for x in tasks:
        print(x)

def test_get_task_by_id():
    task=data.get_task_by_id("2019102518293432135")
    print(task)
test_get_task_by_id()