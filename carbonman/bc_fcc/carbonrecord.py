# coding=utf8
from antcloudsdkcore.client import AntCloudClient
  
# 初始化客户端
client = AntCloudClient(
    "https://openapi.antchain.antgroup.com/gateway.do",
    "<your-access-key>",
    "<your-access-secret>"
)

# 构建请求
request = {}
request["app_did"] = "did:mychain:6615e10cfe5c4dcd13534d9e076c74ed5bdcfaae7887ad6aa4f2fdfcb0430df9 "
request["schema_name"] = "table"
request["attributes.n.name"] = "key"
request["attributes.n.value"] = "value"
request["method"] = "blockchain.appex.solution.fastnotary.save"
request["version"] = "1.0"
request["product_instance_id"] = "7304XXXXXXXX"
request["region_name"] = "CN-HANGZHOU-FINANCE"

# 发送请求，并且获取响应结果
response = client.execute(request)
