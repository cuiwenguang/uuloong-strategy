## UULOONG-STRATEGY 接口文档

### 基本概念

UULOONG-STRATEGY 是用于进行广告策略调整的项目，整个项目由 Flask 构建。
为了程序的安全性，所有访问请求都需要加上一个 header 用于身份标示。

下面将介绍最基本的 Resource Endpoint。

#### Game

Game Endpoint 泛指游戏本身，是整个项目中的基础单元。其结构如下：

```json
{
	"name": "string",
	"ios_access_key": "string",
	"android_access_key": "string"
}
```

其中：

Key | 类型 | 描述
---|---|---
name | string |游戏名称
ios\_access\_key |string| iOS 应用访问钥匙
android\_access\_key |string| Android 应用访问钥匙

#### Campaign

Campaign Endpoint 是对广告商信息的描述：

```json
{
	"name": "string",
	"supplier": "string",
	"access_info": "string",
	"enum": "string"
}
```

其中：

Key | 类型 | 描述
---|---|---
name | string | 广告商自定义名称，即对于本广告条目自定义的名词，可以为任何值
supplier |string| 广告商名词，如 "Admob"
access_info |string| 本广告商基础的访问信息，API key 或账号密码等（可不填）
enum |string| enum 是用于和客户端之间沟通的字符串，如 “kCampaignChartBoost” 本字段一旦确定不再改变

#### Event

Event Endpoint 是对于游戏中广告触发事件的具体描述：

```json
{
	"game_id": "string",
	"name": "string",
	"probability": float
}
```

其中：

Key | 类型 | 描述
---|---|---
game_id | string | Game 对象的 ID，事件是基于 Game 之上的
name | string| 事件名词
probability | float | 事件触发概率，值域：(0, 1)

#### Strategy

Strategy Endpoint 是对于游戏中广告策略的具体描述：

```json
{
	"game_id": "string",
	"country": "string",
	"device_model": "string",
	"banner_campaign": [{
		"campaign_id": "string",
		"z_index": int,
		"tactic": {
			"mins": float,
			"times": float
		}
	}],
	"interstitial_campaign": [{
		"campaign_id": "string",
		"z_index": int,
		"tactic": {
			"mins": float,
			"times": float
		}
	}],
	"video_campaign": [{
		"campaign_id": "string",
		"z_index": int,
		"tactic": {
			"mins": float,
			"times": float
		}
	}]
}
```

其中：

Key | 类型 | 描述
---|---|---
game_id | string | Game 对象的 ID，策略是基于 Game 之上的
country | string| 事件名词
device_model | string | 设备类型
banner_campaign | List(Advertise) | Banner 类型
interstitial_campaign | List(Advertise) | Interstitial 类型
video_campaign | List(Advertise) | Video 类型

Advertise:

Key | 类型 | 描述
---|---|---
campaign_id | string | Campaign 对象的 ID，针对于具体广告的配置信息
tactic | Tactic| 广告策略
z_index | string | 广告的优先级，从 1000 开始降幂

Tactic:

Key | 类型 | 描述
---|---|---
mins | float | 广告每次显示几分钟，理论上和 times 字段，二选一
times | float | 广告每次显示几次，理论上和 mins 字段，二选一


## 接口

### 游戏接口

#### 获取所有游戏

`GET /api/v1.0/games/`

```http
GET /api/v1.0/games/ HTTP/1.1
X-BYGame-Manager-Token: xxxxxxxxxxxx
```

返回数据：

List(Game)

请参照 Game Resources

#### 获取指定游戏

`GET /api/v1.0/games/id`

```http
GET /api/v1.0/games/2314gh1ui3gh2ui4h1 HTTP/1.1
X-BYGame-Manager-Token: xxxxxxxxxxxx
```

返回数据：

Game

请参照 Game Resources

#### 创建游戏

`POST /api/v1.0/games`

```http
POST /api/v1.0/games HTTP/1.1
Content-Type: application/json
X-BYGame-Manager-Token: xxxxxxxxxxxx
{Game Resources}
```

返回数据：

Game

请参照 Game Resources

#### 更新

`PUT /api/v1.0/games/id`

```http
PUT /api/v1.0/games/h4ui123h4g1uih341ui2 HTTP/1.1
Content-Type: application/json
X-BYGame-Manager-Token: xxxxxxxxxxxx
{
	"name": "string" // 只可对游戏名进行修改
}
```

返回数据：

Game

请参照 Game Resources


#### 删除

`DELETE /api/v1.0/games/id`

```http
DELETE /api/v1.0/games/h4ui123h4g1uih341ui2 HTTP/1.1
Content-Type: application/json
X-BYGame-Manager-Token: xxxxxxxxxxxx
```

返回数据：{}

### 广告接口

#### 获取所有广告

`GET /api/v1.0/campaigns/`

```http
GET /api/v1.0/campaigns/ HTTP/1.1
X-BYGame-Manager-Token: xxxxxxxxxxxx
```

返回数据：

List(Campaign)

请参照 Campaign Resources

#### 获取指定广告

`GET /api/v1.0/campaigns/id`

```http
GET /api/v1.0/campaigns/2314gh1ui3gh2ui4h1 HTTP/1.1
X-BYGame-Manager-Token: xxxxxxxxxxxx
```

返回数据：

Campaign

请参照 Campaign Resources

#### 创建广告

`POST /api/v1.0/campaigns `

```http
POST /api/v1.0/campaigns HTTP/1.1
Content-Type: application/json
X-BYGame-Manager-Token: xxxxxxxxxxxx
{Campaign Resources}
```

返回数据：

Campaign

请参照 Campaign Resources

#### 更新广告

`PUT /api/v1.0/campaigns/id`

```http
PUT /api/v1.0/campaigns/h4ui123h4g1uih341ui2 HTTP/1.1
Content-Type: application/json
X-BYGame-Manager-Token: xxxxxxxxxxxx
{Campaign Resources}
```

返回数据：

Campaign

请参照 Campaign Resources


#### 删除广告

`DELETE /api/v1.0/campaigns/id`

```http
DELETE /api/v1.0/campaigns/h4ui123h4g1uih341ui2 HTTP/1.1
Content-Type: application/json
X-BYGame-Manager-Token: xxxxxxxxxxxx
```

返回数据：{}

### 事件接口

请注意，对于所有事件接口需要加入以下query_string：

`?game_id=xxxxxxx`

用于标示事件操作是正对于哪个游戏


#### 获取所有事件

`GET /api/v1.0/events?game_id=xxxxxxx`

```http
GET /api/v1.0/events?game_id=xxxxxxx HTTP/1.1
X-BYGame-Manager-Token: xxxxxxxxxxxx
```

返回数据：

List(Event)

请参照 Event Resources

#### 获取指定事件

`GET /api/v1.0/events/id?game_id=xxxxxxx`

```http
GET /api/v1.0/events/2314gh1ui3gh2ui4h1?game_id=xxxxxxx HTTP/1.1
X-BYGame-Manager-Token: xxxxxxxxxxxx
```

返回数据：

Event

请参照 Event Resources

#### 创建事件

`POST /api/v1.0/events?game_id=xxxxxxx `

```http
POST /api/v1.0/events?game_id=xxxxxxx HTTP/1.1
Content-Type: application/json
X-BYGame-Manager-Token: xxxxxxxxxxxx
{Event Resources}
```

返回数据：

Event

请参照 Event Resources

#### 更新事件

`PUT /api/v1.0/events/id?game_id=xxxxxxx`

```http
PUT /api/v1.0/events/h4ui123h4g1uih341ui2?game_id=xxxxxxx HTTP/1.1
Content-Type: application/json
X-BYGame-Manager-Token: xxxxxxxxxxxx
{Event Resources} // game_id 不可修改
```

返回数据：

Event

请参照 Event Resources


#### 删除事件

`DELETE /api/v1.0/events/id?game_id=xxxxxxx`

```http
DELETE /api/v1.0/events/h4ui123h4g1uih341ui2?game_id=xxxxxxx HTTP/1.1
Content-Type: application/json
X-BYGame-Manager-Token: xxxxxxxxxxxx
```

返回数据：{}

### 策略接口

请注意，对于所有策略接口需要加入以下query_string：

`?game_id=xxxxxxx`

用于标示策略操作是针对于哪个游戏


#### 获取所有策略

`GET /api/v1.0/strategies?game_id=xxxxxxx`

```http
GET /api/v1.0/strategies?game_id=xxxxxxx HTTP/1.1
X-BYGame-Manager-Token: xxxxxxxxxxxx
```

返回数据：

List(Strategy)

请参照 Strategy Resources

#### 获取指定策略

`GET /api/v1.0/strategies/id?game_id=xxxxxxx`

```http
GET /api/v1.0/strategies/2314gh1ui3gh2ui4h1?game_id=xxxxxxx HTTP/1.1
X-BYGame-Manager-Token: xxxxxxxxxxxx
```

返回数据：

Strategy

请参照 Strategy Resources

#### 创建策略

`POST /api/v1.0/strategies?game_id=xxxxxxx `

```http
POST /api/v1.0/strategies?game_id=xxxxxxx HTTP/1.1
Content-Type: application/json
X-BYGame-Manager-Token: xxxxxxxxxxxx
{Strategy Resources}
```

返回数据：

Strategy

请参照 Strategy Resources

#### 更新策略

`PUT /api/v1.0/strategies/id?game_id=xxxxxxx`

```http
PUT /api/v1.0/strategies/h4ui123h4g1uih341ui2?game_id=xxxxxxx HTTP/1.1
Content-Type: application/json
X-BYGame-Manager-Token: xxxxxxxxxxxx
{Strategy Resources} // game_id 不可修改
```

返回数据：

Strategy

请参照 Strategy Resources


#### 删除策略

`DELETE /api/v1.0/strategies/id?game_id=xxxxxxx`

```http
DELETE /api/v1.0/strategies/h4ui123h4g1uih341ui2?game_id=xxxxxxx HTTP/1.1
Content-Type: application/json
X-BYGame-Manager-Token: xxxxxxxxxxxx
```

返回数据：{}

#### 手机端获取策略
`GET /api/v1.0/strategy

手机端需要发送 "X-BYGame-Application-Token" 作为 header， 需要注意的是，"X-BYGame-Application-Token" 的值是由 Game resources 创建时生成的

```http
GET /api/v1.0/strategy HTTP/1.1
X-BYGame-Application-Token: xxxxxxxxxxxx
```

返回数据：

修改版 Strategy，结构如下

```json
{
	"game_id": "string",
	"country": "string",
	"device_model": "string",
	"banner_campaign": [{
		"campaign": "string", // 广告商对象的 Enum 字段
		"z_index": int,
		"tactic": {
			"mins": float,
			"times": float
		}
	}],
	"interstitial_campaign": [{
		"campaign": "string", // 广告商对象的 Enum 字段
		"z_index": int,
		"tactic": {
			"mins": float,
			"times": float
		}
	}],
	"video_campaign": [{
		"campaign": "string", // 广告商对象的 Enum 字段
		"z_index": int,
		"tactic": {
			"mins": float,
			"times": float
		}
	}]
}