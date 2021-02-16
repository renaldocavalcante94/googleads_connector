from google.ads.google_ads.client import GoogleAdsClient
from google.ads.google_ads.errors import GoogleAdsException
from datetime import datetime


class GoogleAdsAPI():

    def __init__(self,auth_yml_path,customer_id):
        self.client = GoogleAdsClient.load_from_storage(auth_yml_path)
        self.service = self.client.get_service("GoogleAdsService", version="v6")
        self.customer_id = customer_id

    def get_type(self):
        xpto = self.client.get_type("CampaignStatusEnum", version="v6")

        return xpto


    def get_campaigns(self):
        """ Get All Campaigns in the account

        Returns: Retuns a list of dicts representating the attributes of each campaign
        """        

        query = """
        SELECT
            campaign.id,
            campaign.name,
            campaign.advertising_channel_type,
            campaign.campaign_budget,
            campaign.labels,
            campaign.start_date,
            campaign.end_date,
            campaign.status,
            campaign.target_cpm,
            campaign.url_custom_parameters
        FROM campaign
        """

        response = self._execute_query_(query)

        values = []

        for x in response:
            value = {
                "id": x.campaign.id,
                "name": x.campaign.name,
                "advertising_channel_type": x.campaign.advertising_channel_type,
                "campaign_budget": x.campaign.campaign_budget,
                "labels": x.campaign.labels,
                "start_date": x.campaign.start_date,
                "end_date": x.campaign.end_date,
                "status": x.campaign.status,
                "target_cpm": x.campaign.target_cpm,
            }
            values.append(value)

        return values

    def get_campaigns_performance(self,start_date="2020-01-01",end_date="Today"):
        """Get performance by campaign Id and start and end date

        Args:
            start_date (str, optional): Report Start Date. Defaults to "2020-01-01".
            end_date (str, optional): Report End Date. Defaults to "Today".

        Returns:
            list_of_dicts: Return a list of dicts where the values are the columns
        """        
        

        if end_date == "Today":
            end_date = datetime.now().date()

        query = f"""
        SELECT
            campaign.id,
            segments.date,
            metrics.all_conversions,
            metrics.average_cpc,
            metrics.average_cpe,
            metrics.average_cpm,
            metrics.average_cpv,
            metrics.average_page_views,
            metrics.average_time_on_site,
            metrics.bounce_rate,
            metrics.clicks,
            metrics.cost_micros,
            metrics.impressions,
            metrics.interactions
        FROM campaign
        WHERE segments.date >= '{start_date}'
            AND segments.date <= '{end_date}'
        ORDER BY segments.date ASC
        """

        response = self._execute_query_(query)

        values = []
        
        for x in response:
            value = {
                "campaign_id": x.campaign.id,
                "date": x.segments.date,
                "all_conversions": x.metrics.all_conversions,
                "average_cpc": x.metrics.average_cpc,
                "average_cpe": x.metrics.average_cpe,
                "average_cpm": x.metrics.average_cpm,
                "average_cpv": x.metrics.average_cpv,
                "average_page_views": x.metrics.average_page_views,
                "average_time_on_site": x.metrics.average_time_on_site,
                "bounce_rate": x.metrics.bounce_rate,
                "clicks": x.metrics.clicks,
                "cost": (x.metrics.cost_micros/1000000),
                "impressions": x.metrics.impressions,
                "interactions": x.metrics.interactions,
            }

            values.append(value)

        return values

    def _execute_query_(self,query):
        response = self.service.search(self.customer_id,query,9999)

        return response



