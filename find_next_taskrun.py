import sys
import croniter
import datetime

def get_formated_time(a_datetime):
    format_time_str = '%H:%M'
    return a_datetime.time().strftime(format_time_str)

def get_dates_from_now(a_datetime):
    dates_from_now = (datetime.datetime.date(a_datetime) - datetime.date.today()).days
    if dates_from_now == 0:
        return "today"
    if dates_from_now == 1:
        return "tommorow"
    else:
        return 'after ' + str(dates_from_now) + ' days'

def get_tasks_and_their_run_time(tasks):
        time_schedule = []
        task_names = []
        for task in tasks:
            minute, hour, task_name = task.split()
            time_schedule.append(minute + ' ' + hour +' * * *' )
            task_names.append(task_name)
        return task_names, time_schedule

def get_given_time_as_datetime_today(specific_min_str):
    format_datetime_str = '%Y-%m-%d %H:%M'
    specific_datetime_str = str(datetime.date.today()) + ' ' + specific_min_str
    specific_datetime = datetime.datetime.strptime(specific_datetime_str, format_datetime_str)
    specific_datetime -= datetime.timedelta(minutes=1)   #Reduce datetime by a minute so as tasks to fire at current time
    return specific_datetime

def main():
    specific_min_str = sys.argv[1]
    tasks = sys.stdin.read().splitlines()

    task_names, time_schedule = get_tasks_and_their_run_time(tasks)
    specific_datetime = get_given_time_as_datetime_today(specific_min_str)

    for i, task in enumerate(time_schedule):
        cron = croniter.croniter(task, specific_datetime)
        nextrun = cron.get_next(datetime.datetime)
        output = get_formated_time(nextrun) + ' ' + get_dates_from_now(nextrun) + ' - ' + task_names[i]
        print (output)

if __name__ == '__main__':
    main()

