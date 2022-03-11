-- 计算复购率(每个月)
create table order_info(
    order_id string comment '订单号',
    user_id string comment '用户id',
    create_time string comment '创建时间',
    payAmount double comment '金额'
);

-- 1.计算每个月的用户
select
    month(create_time) as dt,
    user_id
from
    order_info
group by
    month(create_time),
    user_id;

-- 2.计算每个月的总用户数
select
    month(create_time) as dt,
    count(distinct user_id) as total
from
    order_info
group by
    month(create_time);

-- 3.计算每个月复购数
select
    t1.dt,
    t2.dt,
    count(distinct t2.user_id)
from
    (
        select
            month(create_time) as dt,
            user_id
        from
            order_info
        group by
            month(create_time),
            user_id
    ) t1
    left join (
        select
            month(create_time) as dt,
            user_id
        from
            order_info
        group by
            month(create_time),
            user_id
    ) t2 on t1.user_id = t2.user_id
    and t1.dt < t2.dt
group by
    t1.dt,
    t2.dt;

-- 4.复购率=复购数/总数
select
    t3.nmonth,
    t3.rmonth,
    t3.repeatnum,
    total,
    t3.repeatnum / total as repeatratio
from
    (
        select
            t1.dt as nmonth,
            t2.dt as rmonth,
            count(distinct t2.user_id) as repeatnum
        from
            (
                select
                    month(create_time) as dt,
                    user_id
                from
                    order_info
                group by
                    month(create_time),
                    user_id
            ) t1
            left join (
                select
                    month(create_time) as dt,
                    user_id
                from
                    order_info
                group by
                    month(create_time),
                    user_id
            ) t2 on t1.user_id = t2.user_id
            and t1.dt < t2.dt
        group by
            t1.dt,
            t2.dt
    ) t3
    left join (
        select
            month(create_time) as dt,
            count(distinct user_id) as total
        from
            order_info
        group by
            month(create_time)
    ) t4 on t3.nmonth == t4.dt;

-- solution2
select
    firstmon,
    count(user_id) as 'newadd',
    sum(fugou) as 'fugou',
    sum(fugou) / count(user_id) as 'fugouratio'
from
    (
        select
            t1.firstmon,
            t1.user_id,
            if(count(t1.user_id) > 1, 1, 0) as fugou
        from
            (
                select
                    user_id,
                    month(min(create_time)) as firstmon
                from
                    order_info
                group by
                    user_id
            ) t1
            left join order_info t2 on t1.user_id = t2.user_id
            and t1.firstmon = month(t2.create_time)
        group by
            t1.firstmon,
            t1.user_id
    ) t3
group by
    firstmon;

select
    max(hire_date)
from
    employees
group by
    hire_date
order by
    hire_date desc
select
    hire_date,
    rownumber() over(
        order by
            hire_date desc
    )
from
    employees;



select
    emp_no,
    salary,
    last_name,
    first_name
from
    (
        select
            t1.emp_no,
            t1.first_name,
            t2.last_name,
            DENSE_RANK() over (
                order by
                    desc
            ) rowid
        from
            employees t1
            join salaries t2 on t1.emp_no = t2.emp_no
    ) t3
where
    rowid = 2

select t1.emp_no,max(t1.salary),t2.last_name,t2.first_name
from salaries t1 join employees t2 on t1.emp_no=t2.emp_no
and t1.salary not in (select max(salary) from salaries)


