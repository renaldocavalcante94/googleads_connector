# Google Ads Connector

## Objective
The main objective of this Connector is to make easier to get campaigns, and campaigns performance

## Needed Libs
```
pip install google-ads
```

## How to Use

### Authentication
Follow this steps to get **client_id** and **client_secret** and a **refresh_token**
- [GoogleDocs](https://developers.google.com/google-ads/api/docs/client-libs/python/oauth-desktop?hl=en)

You wil need a **googleads.yaml**  file , follow the example below

The developer token and Login Customer ID are related to your google ads account. To get them Follow this step
[DeveloperToken](https://developers.google.com/google-ads/api/docs/first-call/dev-token)

**login_customer_id** is the MCC id Login , used to get the basic access to the Developer toke

```
# OAuth2 configuration
###############################################################################
# The below configuration parameters are used to authenticate using the       #
# recommended OAuth2 flow. For more information on authenticating with OAuth2 #
# see: https://developers.google.com/google-ads/api/docs/oauth/overview       #
###############################################################################
developer_token: XXXXXXXXXXXXXXXXXXXX
client_id: XXXXXXXXXXXXXXXXXXXX
client_secret: XXXXXXXXXXXXXXXXXXXX
refresh_token: XXXXXXXXXXXXXXXXXXXX

# Login customer ID configuration
###############################################################################
# Required for manager accounts only: Specify the login customer ID used to   #
# authenticate API calls. This will be the customer ID of the authenticated   #
# manager account. It should be set without dashes, for example: 1234567890   #
# instead of 123-456-7890. You can also specify this later in code if your    #
# application uses multiple manager account + OAuth pairs.                    #
###############################################################################
login_customer_id: XXXXXXXXXXXXXXXXXXXX
# Service Account configuration
###############################################################################
# To authenticate with a service account add the appropriate values to the    #
# below configuration parameters and remove the four OAuth credentials above. #
# The "json_key_file_path" value should be a path to your local private       #
# key json file, and "impersonated_email" should be the email address that is #
# being used to impersonate the credentials making requests. for more         #
# information on service accounts, see:                                       #
# https://developers.google.com/google-ads/api/docs/oauth/service-accounts    #
###############################################################################
# json_key_file_path: INSERT_PATH_TO_JSON_KEY_FILE_HERE
# impersonated_email: INSERT_DOMAIN_WIDE_DELEGATION_ACCOUNT

# Logging configuration
###############################################################################
# Below you may specify the logging configuration. This will be provided as   #
# an input to logging.config.dictConfig. Use the "level" block under the root #
# logger configuration to adjust the logging level. Note in the "format"      #
# field that log messages are truncated to 5000 characters by default. You    #
# can change this to any length by removing the ".5000" portion or changing   #
# it to a different number.                                                   #
# #############################################################################
# logging:
  # version: 1
  # disable_existing_loggers: False
  # formatters:
    # default_fmt:
      # format: '[%(asctime)s - %(levelname)s] %(message).5000s'
      # datefmt: '%Y-%m-%d %H:%M:%S'
  # handlers:
    # default_handler:
      # class: logging.StreamHandler
      # formatter: default_fmt
  # loggers:
    # "":
      # handlers: [default_handler]
      # level: INFO
```
#### Developer Token Basic Access
To make the requests the Developer token must have at leas a **basic** acess, to get that follow these steps

1. in a MCC Account
2. Go in the right-up corner menu Tools
3. More tools API Center
4. Apply for Basic Access
5. Fill the form with your company infos and Follow the talk to google assistant until you get your token approval

#### Customer Id
The customer Id used in the class **GoogleAdsAPI** is referreed to the normal Ads Account and not MCC.


## Use

```
from google_ads.py import GoogleAdsAPI()

ads = GoogleAdsAPI("./googleads.yaml",111-111-1111)

ads.get_campaigns() # Wil Return All campaigns
ads.get_campaigns_performance(start_date="2018-01-01",end_date="Today") #Will get all companyes performance values for all campaigns
```





