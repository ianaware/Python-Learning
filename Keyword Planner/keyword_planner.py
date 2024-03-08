import csv
from google.ads.google_ads.client import GoogleAdsClient
from google.ads.google_ads.errors import GoogleAdsException

def get_keyword_ideas(client, customer_id, keyword_text):
    # Get the service for keyword planning
    keyword_plan_idea_service = client.get_service("KeywordPlanIdeaService")

    # Set up the request: Here you configure language, location, and the keyword seed
    # Note: IDs for location and language should be replaced with actual values
    request = client.get_type("GenerateKeywordIdeasRequest")
    request.customer_id = customer_id
    request.language_id = '1000'  # Example ID for English
    request.geo_target_constants = ['2124']  # Example ID for Thailand
    request.include_adult_keywords = False  # Based on your requirements
    request.keyword_plan_network = client.enums.KeywordPlanNetworkEnum.GOOGLE_SEARCH
    request.keyword_and_url_seed.keywords.append(keyword_text)

    try:
        # Execute the request
        response = keyword_plan_idea_service.generate_keyword_ideas(request=request)
        # Extract and return keyword ideas
        keyword_ideas = []
        for idea in response.results:
            keyword_ideas.append({
                'text': idea.text,
                'search_volume': idea.keyword_idea_metrics.avg_monthly_searches,
                'competition': idea.keyword_idea_metrics.competition.name,
                'cpc': idea.keyword_idea_metrics.average_cpc.micros / 1e6
            })
        return keyword_ideas
    except GoogleAdsException as ex:
        # Handle API errors
        print(f"Request had errors: {ex}")
        return []

def save_keywords_to_csv(keywords, filename="keywords.csv"):
    # Save the list of keywords to a CSV file
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Keyword", "Search Volume", "Competition", "CPC"])  # Add more fields as needed
        for keyword in keywords:
            writer.writerow([keyword['text'], keyword['search_volume'], keyword['competition'], keyword['cpc']])  # Map according to your data structure

def main():
    # Initialize the Google Ads client
    google_ads_client = GoogleAdsClient.load_from_storage()
    customer_id = 'your-customer-id'  # Replace with your Google Ads customer ID
    
    # Ask for user input
    keyword_text = input("Enter the keyword you want to get ideas for: ")

    # Fetch keyword ideas
    keyword_ideas = get_keyword_ideas(google_ads_client, customer_id, keyword_text)

    # Print top 50 keywords (modify according to how your data is structured)
    print("Top 50 keyword ideas:")
    for i, idea in enumerate(keyword_ideas[:50], start=1):
        print(f"{i}. {idea['text']} (Search Volume: {idea['search_volume']}, Competition: {idea['competition']}, CPC: {idea['cpc']})")  # Adapt based on actual data structure

    # Ask if user wants to export to CSV
    export_answer = input("Do you want to output the results as a CSV file? (yes/no): ")
    if export_answer.lower() == 'yes':
        save_keywords_to_csv(keyword_ideas, "keyword_ideas.csv")
        print("Keywords have been saved to keyword_ideas.csv")

if __name__ == "__main__":
    main()
