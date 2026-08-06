# -*- coding: utf-8 -*-
import webbrowser
import os

html_content = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
    <title>计算机网络知识图谱 - 人机协同课堂 | 知识点讲解+例题</title>
    <script src="https://cdn.jsdelivr.net/npm/echarts@5.5.0/dist/echarts.min.js"></script>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', 'PingFang SC', Roboto, 'Helvetica Neue', sans-serif;
            background: linear-gradient(145deg, #f0f7ff 0%, #e9eef5 100%);
            min-height: 100vh;
            padding: 20px;
        }
        .container {
            max-width: 1500px;
            margin: 0 auto;
            background: rgba(255,255,255,0.6);
            border-radius: 2rem;
            backdrop-filter: blur(2px);
            box-shadow: 0 20px 35px -12px rgba(0,0,0,0.2);
            padding: 1rem 1.5rem 1.5rem 1.5rem;
        }
        h1 {
            font-size: 1.8rem;
            font-weight: 700;
            background: linear-gradient(135deg, #1e2b5c, #2c3e6d);
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
        }
        .sub {
            color: #4a627a;
            border-left: 4px solid #3b82f6;
            padding-left: 14px;
            margin: 0.5rem 0 1.2rem 0;
            font-weight: 500;
            font-size: 0.95rem;
        }
        .dashboard { display: flex; flex-wrap: wrap; gap: 20px; }
        .graph-card {
            flex: 3;
            min-width: 0;
            background: #ffffffdd;
            border-radius: 28px;
            box-shadow: 0 8px 20px rgba(0,0,0,0.08);
            padding: 1rem;
        }
        .info-card {
            flex: 1.3;
            min-width: 280px;
            background: #ffffffdd;
            border-radius: 28px;
            box-shadow: 0 8px 20px rgba(0,0,0,0.08);
            padding: 1.2rem;
            display: flex;
            flex-direction: column;
            max-height: 620px;
            overflow-y: auto;
        }
        .graph-container { width: 100%; height: 580px; background: #fefefe; border-radius: 24px; }
        .section-title {
            font-size: 1.2rem;
            font-weight: 700;
            border-left: 5px solid #3b82f6;
            padding-left: 12px;
            margin: 0.8rem 0 0.6rem 0;
            color: #1e293b;
        }
        .section-title:first-of-type { margin-top: 0; }
        .node-name-big {
            font-size: 1.4rem;
            font-weight: 800;
            background: linear-gradient(135deg, #1f3a6b, #2b4c7c);
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
            margin-bottom: 5px;
        }
        .explain-box {
            background: #f1f5f9;
            border-radius: 20px;
            padding: 12px 14px;
            margin-bottom: 20px;
            border: 1px solid #e2e8f0;
        }
        .explain-text { font-size: 0.88rem; line-height: 1.45; color: #0f172a; }
        .example-box {
            background: #fff7ed;
            border-left: 4px solid #f97316;
            border-radius: 18px;
            padding: 12px 14px;
            margin-bottom: 16px;
        }
        .example-title { font-weight: 700; color: #c2410c; font-size: 0.85rem; margin-bottom: 8px; }
        .example-content {
            font-size: 0.82rem;
            color: #2c3e2f;
            background: #fff;
            padding: 8px 10px;
            border-radius: 14px;
            white-space: pre-wrap;
        }
        .interact-tip {
            background: #eef2ff;
            border-radius: 18px;
            padding: 12px;
            font-size: 0.75rem;
            color: #1e40af;
            margin-top: 12px;
        }
        .legend {
            display: flex;
            flex-wrap: wrap;
            gap: 12px;
            margin-top: 12px;
            margin-bottom: 8px;
            font-size: 0.7rem;
            justify-content: center;
        }
        .badge { width: 14px; height: 14px; border-radius: 20px; display: inline-block; }
        footer { text-align: center; margin-top: 1.5rem; font-size: 0.7rem; color: #4b5563; }
        @media (max-width: 780px) {
            .graph-container { height: 450px; }
            .info-card { flex: 1; max-height: 500px; }
        }
    </style>
</head>
<body>
<div class="container">
    <div style="display: flex; justify-content: space-between; align-items: baseline; flex-wrap: wrap;">
        <div>
            <h1>计算机网络 · 智慧知识图谱</h1>
            <div class="sub">人机协同课堂 | 基于《2026王道考研》| 点击节点 → 知识点讲解 + 经典例题</div>
        </div>
        <div class="legend">
            <span><i class="badge" style="background: #5470c6;"></i> 核心层</span>
            <span><i class="badge" style="background: #fac858;"></i> 协议/子领域</span>
            <span><i class="badge" style="background: #ee6666;"></i> 关键技术</span>
            <span><i class="badge" style="background: #73c0de;"></i> 重要知识点</span>
        </div>
    </div>
    <div class="dashboard">
        <div class="graph-card">
            <div id="knowledgeGraph" class="graph-container"></div>
        </div>
        <div class="info-card">
            <div class="node-name-big" id="currentNodeTitle">计算机网络体系</div>
            <div class="section-title">知识点讲解</div>
            <div id="explanationArea" class="explain-box">
                <div class="explain-text" id="explanationText">点击左侧图谱中的任意节点，右侧将展示该知识点的详细讲解，并配备一道典型例题。</div>
            </div>
            <div class="section-title">配套例题</div>
            <div id="exampleArea" class="example-box">
                <div class="example-title">例题</div>
                <div class="example-content" id="exampleContent">例如点击"CSMA/CD"可查看以太网最短帧长计算题。</div>
            </div>
            <div class="interact-tip">
                <strong>互动学习</strong><br>
                单击节点获取深度讲解+真题风格例题。<br>
                拖拽/缩放探索协议栈关联。
            </div>
        </div>
    </div>
    <footer>基于26版《计算机网络》考研复习指导 | 知识点精讲 + 经典例题 | 支撑师生机三元协同课堂</footer>
</div>

<script>
    const knowledgeBase = {
        osi: { name: "OSI参考模型", explain: "国际标准化组织提出的7层模型：物理层、数据链路层、网络层、传输层、会话层、表示层、应用层。核心概念：服务、接口、协议。各层功能独立，下层为上层提供服务。", example: "[例题] 在OSI参考模型中，自下而上第一个提供端到端服务的层是？\\nA.数据链路层 B.传输层 C.会话层 D.应用层\\n[解析] 传输层提供进程间端到端通信，答案为B。" },
        tcpip: { name: "TCP/IP模型", explain: "4层模型：网络接口层、网际层(IP)、传输层(TCP/UDP)、应用层。IP提供无连接不可靠数据报，TCP面向连接可靠传输。", example: "[例题] TCP/IP模型的网际层提供哪种服务？\\n[解析] 无连接不可靠的数据报服务，尽最大努力交付。" },
        five_layer: { name: "五层体系结构", explain: "综合OSI与TCP/IP优点：物理层、数据链路层、网络层、传输层、应用层。考研常用，便于理解数据封装过程。", example: "[例题] 在五层模型中，路由器实现哪几层功能？\\n[解析] 物理层、数据链路层、网络层。" },
        phy: { name: "物理层", explain: "传输比特流，定义机械/电气/功能/过程特性。典型设备：中继器、集线器。", example: "[例题] 某网络在物理层规定信号电平+10V~+15V表示0，-10V~-15V表示1，属于哪类特性？\\n[解析] 电气特性。" },
        nyquist: { name: "奈奎斯特定理", explain: "理想低通信道下，极限码元速率=2W Baud，极限数据率=2W log2(V) b/s。避免码间串扰。", example: "[例题] 带宽为4kHz的无噪声信道，采用16种物理状态，最大传输速率？\\n[解析] 2*4k*log2(16)=32kb/s。" },
        shannon: { name: "香农定理", explain: "有噪声信道极限速率=W log2(1+S/N) b/s。信噪比30dB对应S/N=1000。", example: "[例题] 带宽3kHz，信噪比30dB，最大数据率？\\n[解析] 3k*log2(1001)≈30kb/s。" },
        encoding: { name: "编码与调制", explain: "曼彻斯特编码（自同步）、差分曼彻斯特、NRZ、QAM调制等。以太网采用曼彻斯特编码。", example: "[例题] 曼彻斯特编码中，码元中间的跳变的作用是什么？\\n[解析] 既作为时钟信号，又作为数据信号。" },
        datalink: { name: "数据链路层", explain: "封装成帧、透明传输、差错控制(CRC)、流量控制。MAC子层负责介质访问。", example: "[例题] PPP协议采用哪种方法实现透明传输？\\n[解析] 异步线路用字节填充，同步线路用零比特填充。" },
        csmacd: { name: "CSMA/CD", explain: "先听后发，边听边发，冲突停发，随机重发。争用期=2τ，最短帧长=争用期×数据传输速率。以太网最短64B。", example: "[例题] 10Mb/s以太网，最大距离2km，信号速率2e8m/s，最小帧长？\\n[解析] 传播时延=10us，往返20us，最小帧长=10M×20us=200bit。" },
        csmaca: { name: "CSMA/CA", explain: "无线局域网使用，RTS/CTS预约信道，避免冲突。ACK确认保证可靠。", example: "[例题] CSMA/CA中，隐藏站问题如何解决？\\n[解析] 通过RTS/CTS帧预约信道，其他站设置NAV。" },
        sw_arq: { name: "滑动窗口协议", explain: "停止-等待(WT=1,WR=1)、后退N帧(WT>1,WR=1)、选择重传(WT>1,WR>1)。", example: "[例题] GBN协议发送窗口大小为4，采用2bit序号，能否正常工作？\\n[解析] 不能，2bit序号最大窗口为2^2-1=3。" },
        vlan: { name: "VLAN虚拟局域网", explain: "802.1Q帧插入4字节标签，分割广播域，基于端口/MAC划分。", example: "[例题] VLAN划分方式不包括？\\n[解析] 不包括基于用户名划分。" },
        ethernet: { name: "以太网与MAC帧", explain: "MAC地址6字节，帧格式：前导码+目的地址+源地址+类型+数据(46~1500)+FCS。", example: "[例题] 以太网帧数据字段至少多少字节？\\n[解析] 64-18=46字节。" },
        network: { name: "网络层", explain: "IP协议、路由选择、分组转发、拥塞控制。虚电路vs数据报。", example: "[例题] 路由器转发主要依据什么地址？\\n[解析] 目的IP地址，最长前缀匹配。" },
        ipv4: { name: "IPv4", explain: "32位地址，首部20~60B。重要字段：TTL、协议、首部检验和、分片标识/标志/片偏移。", example: "[例题] IPv4首部中哪个字段防止分组无限循环？\\n[解析] TTL(生存时间)，每跳减1。" },
        cidr: { name: "CIDR与路由聚合", explain: "无分类编址斜线记法，最长前缀匹配。路由聚合减少路由表项。", example: "[例题] 地址块192.168.10.0/20包含的IP范围？\\n[解析] 192.168.0.0~192.168.15.255。" },
        nat: { name: "NAT", explain: "私有地址转全球IP，NAPT使用端口映射。私有地址段：10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16。", example: "[例题] NAT路由器转发时修改什么？\\n[解析] 源IP地址和源端口号。" },
        arp: { name: "ARP协议", explain: "IP解析为MAC，同一局域网广播ARP请求，单播响应。", example: "[例题] ARP请求帧的目的MAC地址？\\n[解析] FF-FF-FF-FF-FF-FF(广播)。" },
        icmp: { name: "ICMP协议", explain: "差错报告与询问。Ping使用回送请求/回答，Traceroute使用时间超过报文。", example: "[例题] Traceroute利用了ICMP哪种报文？\\n[解析] 时间超过报文。" },
        dhcp: { name: "DHCP", explain: "动态分配IP，应用层/UDP。发现报文源IP=0.0.0.0，目的IP=255.255.255.255。", example: "[例题] DHCP发现报文的目的IP？\\n[解析] 255.255.255.255(受限广播)。" },
        routing: { name: "路由算法", explain: "距离-向量(RIP，跳数)、链路状态(OSPF，代价)、路径向量(BGP)。", example: "[例题] RIP中跳数为16表示什么？\\n[解析] 网络不可达。" },
        rip: { name: "RIP协议", explain: "基于距离向量，UDP封装，周期30s交换路由表。最大跳数15，坏消息传播慢。", example: "[例题] RIP中路由器收到邻居路由表距离加1的原因？\\n[解析] 经过一跳，距离度量增加。" },
        ospf: { name: "OSPF协议", explain: "链路状态，Dijkstra算法，IP协议89，区域划分，收敛快。", example: "[例题] OSPF使用什么算法计算最短路径？\\n[解析] Dijkstra最短路径算法。" },
        bgp: { name: "BGP协议", explain: "AS间路由，路径向量，TCP封装，使用eBGP和iBGP。", example: "[例题] BGP采用哪种传输层协议？\\n[解析] TCP，保证可靠性。" },
        ipv6: { name: "IPv6", explain: "128位地址，固定首部40B，无检验和，邻居发现替代ARP，不允许中间分片。", example: "[例题] IPv6地址简化写法：8:D0:123:C0DEF:89A完整形式？\\n[解析] 0008:0000:0000:0000:00D0:0123:CDEF:089A。" },
        transport: { name: "传输层", explain: "端到端通信，端口号标识进程。TCP可靠面向连接，UDP高效无连接。", example: "[例题] 传输层复用/分用依靠什么？\\n[解析] 端口号。" },
        udp: { name: "UDP协议", explain: "无连接，首部8B，检验和可选，适合实时应用。", example: "[例题] UDP检验和计算需要加入什么？\\n[解析] 12字节伪首部。" },
        tcp: { name: "TCP协议", explain: "面向连接可靠传输，流量控制(rwnd)，拥塞控制(cwnd)。序号、确认、超时重传、快速重传。", example: "[例题] TCP发送窗口大小由什么决定？\\n[解析] min(接收窗口, 拥塞窗口)。" },
        tcp_conn: { name: "TCP连接管理", explain: "三次握手建立，四次挥手释放。SYN消耗序号，FIN消耗序号。", example: "[例题] TCP第二次握手报文SYN和ACK的值？\\n[解析] SYN=1, ACK=1。" },
        tcp_congest: { name: "TCP拥塞控制", explain: "慢开始(指数增长)、拥塞避免(线性增长)、快重传(3冗余ACK)、快恢复。超时事件cwnd=1。", example: "[例题] 拥塞窗口为16KB时超时，ssthresh变为多少？\\n[解析] 8KB，cwnd置1。" },
        app: { name: "应用层", explain: "为用户提供网络服务，常见协议：HTTP、DNS、FTP、SMTP等。", example: "[例题] 电子邮件发送和读取分别用什么协议？\\n[解析] 发送SMTP，读取POP3/IMAP。" },
        dns: { name: "DNS系统", explain: "域名解析，递归/迭代查询，UDP端口53，层次域名空间。", example: "[例题] 本地域名服务器向根域名服务器查询通常采用哪种方式？\\n[解析] 迭代查询。" },
        http: { name: "HTTP协议", explain: "超文本传输，持久/非持久连接，无状态+Cookie。请求方法GET/POST等。", example: "[例题] HTTP/1.1默认使用哪种连接？\\n[解析] 持续连接(流水线方式可选)。" },
        ftp: { name: "FTP协议", explain: "控制连接(21)和数据连接(20)，带外传送。主动PORT模式与被动PASV模式。", example: "[例题] FTP服务器传输文件时使用的端口？\\n[解析] 数据连接默认20端口。" },
        email: { name: "电子邮件", explain: "SMTP发送，POP3/IMAP读取，MIME扩展支持多媒体。", example: "[例题] MIME的作用？\\n[解析] 将非ASCII码数据转换为ASCII码以便SMTP传输。" },
        p2p: { name: "P2P模型", explain: "对等网络，节点既下载又上传，减轻服务器压力。", example: "[例题] P2P相对于C/S的优点是？\\n[解析] 可扩展性好，健壮性强。" }
    };

    const nodesData = [
        { id: "osi", name: "OSI参考模型", category: "layer", size: 28 },
        { id: "tcpip", name: "TCP/IP模型", category: "layer", size: 28 },
        { id: "five_layer", name: "五层体系结构", category: "layer", size: 28 },
        { id: "phy", name: "物理层", category: "layer", size: 26 },
        { id: "nyquist", name: "奈奎斯特定理", category: "tech", size: 24 },
        { id: "shannon", name: "香农定理", category: "tech", size: 24 },
        { id: "encoding", name: "编码与调制", category: "tech", size: 24 },
        { id: "datalink", name: "数据链路层", category: "layer", size: 26 },
        { id: "csmacd", name: "CSMA/CD", category: "protocol", size: 30 },
        { id: "csmaca", name: "CSMA/CA", category: "protocol", size: 28 },
        { id: "sw_arq", name: "滑动窗口协议", category: "tech", size: 28 },
        { id: "vlan", name: "VLAN", category: "tech", size: 24 },
        { id: "ethernet", name: "以太网与MAC帧", category: "protocol", size: 28 },
        { id: "network", name: "网络层", category: "layer", size: 26 },
        { id: "ipv4", name: "IPv4", category: "protocol", size: 30 },
        { id: "cidr", name: "CIDR路由聚合", category: "tech", size: 28 },
        { id: "nat", name: "NAT", category: "tech", size: 24 },
        { id: "arp", name: "ARP协议", category: "protocol", size: 24 },
        { id: "icmp", name: "ICMP协议", category: "protocol", size: 24 },
        { id: "dhcp", name: "DHCP", category: "protocol", size: 24 },
        { id: "routing", name: "路由算法", category: "tech", size: 28 },
        { id: "rip", name: "RIP协议", category: "protocol", size: 24 },
        { id: "ospf", name: "OSPF协议", category: "protocol", size: 24 },
        { id: "bgp", name: "BGP协议", category: "protocol", size: 24 },
        { id: "ipv6", name: "IPv6", category: "protocol", size: 24 },
        { id: "transport", name: "传输层", category: "layer", size: 26 },
        { id: "udp", name: "UDP协议", category: "protocol", size: 24 },
        { id: "tcp", name: "TCP协议", category: "protocol", size: 30 },
        { id: "tcp_conn", name: "TCP连接管理", category: "tech", size: 28 },
        { id: "tcp_congest", name: "TCP拥塞控制", category: "tech", size: 28 },
        { id: "app", name: "应用层", category: "layer", size: 26 },
        { id: "dns", name: "DNS系统", category: "protocol", size: 24 },
        { id: "http", name: "HTTP协议", category: "protocol", size: 28 },
        { id: "ftp", name: "FTP协议", category: "protocol", size: 24 },
        { id: "email", name: "电子邮件", category: "tech", size: 24 },
        { id: "p2p", name: "P2P模型", category: "tech", size: 22 }
    ];

    const linksData = [
        { source: "five_layer", target: "osi" }, { source: "five_layer", target: "tcpip" },
        { source: "osi", target: "phy" }, { source: "osi", target: "datalink" }, { source: "osi", target: "network" },
        { source: "osi", target: "transport" }, { source: "osi", target: "app" },
        { source: "tcpip", target: "network" }, { source: "tcpip", target: "transport" }, { source: "tcpip", target: "app" },
        { source: "phy", target: "nyquist" }, { source: "phy", target: "shannon" }, { source: "phy", target: "encoding" },
        { source: "datalink", target: "csmacd" }, { source: "datalink", target: "csmaca" },
        { source: "datalink", target: "sw_arq" }, { source: "datalink", target: "vlan" }, { source: "datalink", target: "ethernet" },
        { source: "network", target: "ipv4" }, { source: "network", target: "cidr" }, { source: "network", target: "nat" },
        { source: "network", target: "arp" }, { source: "network", target: "icmp" }, { source: "network", target: "dhcp" },
        { source: "network", target: "routing" }, { source: "network", target: "ipv6" },
        { source: "routing", target: "rip" }, { source: "routing", target: "ospf" }, { source: "routing", target: "bgp" },
        { source: "ipv4", target: "cidr" }, { source: "ipv4", target: "nat" },
        { source: "transport", target: "udp" }, { source: "transport", target: "tcp" },
        { source: "tcp", target: "tcp_conn" }, { source: "tcp", target: "tcp_congest" },
        { source: "app", target: "dns" }, { source: "app", target: "http" }, { source: "app", target: "ftp" },
        { source: "app", target: "email" }, { source: "app", target: "p2p" },
        { source: "ethernet", target: "csmacd" }, { source: "ipv4", target: "arp" }, { source: "tcp", target: "http" }
    ];

    const categoryColor = { "layer": "#5470c6", "protocol": "#fac858", "tech": "#ee6666", "detail": "#73c0de" };

    const graphNodes = nodesData.map(node => ({
        id: node.id, name: node.name,
        symbolSize: node.size,
        itemStyle: { color: categoryColor[node.category] },
        category: node.category
    }));

    const graphLinks = linksData.map(link => ({ 
        source: link.source, 
        target: link.target, 
        lineStyle: { color: "#9ca3af", width: 1.3, curveness: 0.2, opacity: 0.7 }
    }));

    const dom = document.getElementById("knowledgeGraph");
    const chart = echarts.init(dom);

    chart.setOption({
        tooltip: { trigger: 'item', formatter: function(params) {
            if (params.dataType === 'node') {
                return '<strong>' + params.name + '</strong><br/>点击右侧查看详解+例题';
            }
            return '';
        } },
        series: [{
            type: 'graph',
            layout: 'force',
            force: { repulsion: 600, edgeLength: [80, 160], gravity: 0.08, friction: 0.1, layoutAnimation: true },
            roam: true,
            draggable: true,
            data: graphNodes,
            links: graphLinks,
            label: {
                show: true,
                position: 'right',
                fontSize: 10,
                offset: [5, 0],
                formatter: function(params) { return params.name; },
                color: '#1f2d3d',
                fontWeight: '500'
            },
            emphasis: { scale: true, label: { show: true, fontWeight: 'bold', fontSize: 11 } },
            lineStyle: { color: 'source', curveness: 0.2, width: 1.2, opacity: 0.6 },
            itemStyle: { borderColor: '#fff', borderWidth: 1.2 },
            edgeSymbol: ['none', 'arrow'],
            edgeSymbolSize: [0, 6]
        }],
        backgroundColor: 'transparent'
    });

    const titleEl = document.getElementById("currentNodeTitle");
    const explainTextEl = document.getElementById("explanationText");
    const exampleContentEl = document.getElementById("exampleContent");

    function updateRightPanel(nodeId) {
        const info = knowledgeBase[nodeId];
        if (info) {
            titleEl.innerText = info.name;
            explainTextEl.innerText = info.explain;
            exampleContentEl.innerHTML = info.example.replace(/\\n/g, '<br>');
        } else {
            titleEl.innerText = "计算机网络体系";
            explainTextEl.innerText = "点击左侧图谱中的任意节点，右侧将展示该知识点的详细讲解。";
            exampleContentEl.innerHTML = "点击节点查看配套例题和解析。";
        }
    }

    updateRightPanel("network");

    chart.on('click', function(params) {
        if (params.dataType === 'node' && params.data) {
            const nodeId = params.data.id;
            if (nodeId && knowledgeBase[nodeId]) {
                updateRightPanel(nodeId);
            }
        }
    });

    window.addEventListener('resize', function() { chart.resize(); });
    setTimeout(function() { chart.resize(); }, 200);
</script>
</body>
</html>
'''

file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "computer_network_knowledge_graph.html")
with open(file_path, "w", encoding="utf-8") as f:
    f.write(html_content)
webbrowser.open(f"file://{file_path}")
print(f"知识图谱已生成并打开: {file_path}")