**GLADOS注册**

1、打开 <https://github.com/glados-network/GLaDOS> ，找到[**\*Register***]，打开链接，填写邮箱进行登录。

2、输入激活码`4MSZ9-1WFJ8-4TLKD-Q1A9Z`，进行激活，获得3天试用。

3、点击签到可以增加一天

**自动签到原理**

1. github 的 actions 可以免费执行代码
2. github 的 actions 可以定时调度

**自动签到方式**

1. fork 此项目
2. 在 fork 出的项目中设置 cookie
3. 修改.github/workflows/auto-checkin.yml 中第10行 `cron 表达式` 并提交
    - 15 * * * * 
    - 16 16 * * *
  
[cron语法参考](https://docs.github.com/cn/free-pro-team@latest/actions/reference/events-that-trigger-workflows#%E8%AE%A1%E5%88%92)


**帮助**
> 打开 chrome, 登录到 glados 控制台, 找到签到按钮, 按 f12, 拿到 cookie  

![image](https://user-images.githubusercontent.com/23112609/96143045-50e80b80-0f35-11eb-8b84-61bcc2f2dac4.png)

> 在fork 出项目下的 `Secrets`中 设置 cookie

![image](https://user-images.githubusercontent.com/23112609/96195429-536f5300-0f7f-11eb-9c97-bf35bfcfdca0.png)

> 在 fork 出项目下的 `actions` 页面, 选中 `glados-checkin-for-http` 可手动触发 workflow;

![image](https://user-images.githubusercontent.com/23112609/96712912-6ac09d00-13d2-11eb-8f06-db18e5249a8e.png)

> 在 fork 出项目下的 `actions` 页面, 查看运行历史日志来确认签到结果

![image](https://user-images.githubusercontent.com/23112609/96226413-29408400-0fc5-11eb-9ef2-044aac8642e1.png)


> 1 2 3 4 5 6 7 8 9 10
