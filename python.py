import requests
import base64

personal_access_token = "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"
api_base_url = "https://api.github.com"
branch = "main"
#owner = "Omairkhalid95"
#repo = 'abc9btcc800000'
#environment = "Production"
file_name = "Readme.md"
file_content = "This is an example file content."
owner = __owner__
repo = __repo__
environment = __environment__




repo_data = {
    "name": repo,
     "description": "This repo is for test porpose",
      "private": False
}
branch_protection_rule = {

"required_status_checks": None,
"enforce_admins": None,
"required_pull_request_reviews" : {
   
    "dismiss_stale_reviews": False,
    "require_code_owner_reviews": True,
    "required_approving_review_count": 2},
    "restrictions": None

}

file_data = {
        "message": "Initial commit",
        "content": base64.b64encode(file_content.encode()).decode("utf-8"),
    }

env_data = {

"wait_timer":30,
 "reviewers":[{"type":"User","id":137157096}]
}







repo_response=  requests.post(f"{api_base_url}/user/repos",json=repo_data,headers= 
{"Authorization": f"Bearer {personal_access_token}"})

print(f"{repo}")
if repo_response.status_code == 201: 
  print("Repo created sucessfully")

  file_response = requests.put(f"{api_base_url}/repos/{owner}/{repo}/contents/{file_name}", json=file_data, headers=
    {"Authorization": f"Bearer {personal_access_token}"})
  print("Readme.md file added")
  print(f"{repo}")
  branch_response=  requests.put(f'{api_base_url}/repos/{owner}/{repo}/branches/{branch}/protection',json=branch_protection_rule,headers= 
{"Authorization": f"Bearer {personal_access_token}"})
     #  url= f"{api_base_url}/repos/{owner}/test-repo-5/branches/{branch}/protection"
  print("2 reviewers  has been added")
  print(f"{repo}")

  env_response=  requests.put(f'{api_base_url}/repos/{owner}/{repo}/environments/{environment}',json=env_data,headers= 
{"Authorization": f"Bearer {personal_access_token}"})
  print(f"Environment: {environment} is created  ")
  print(f"{repo}")





elif repo_response.status_code == 422:
 env_response=  requests.put(f"{api_base_url}/repos/{owner}/{repo}/environments/{environment}",json=env_data,headers= 
{"Authorization": f"Bearer {personal_access_token}"})
 print(f"Environment: {environment} is Updated ")



else:
    print("error during repo creation")
