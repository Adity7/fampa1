from django.shortcuts import render
from .models import Video
import googleapiclient.discovery


# Create your views here.
MAX_RESULTS = 25
PART = "snippet"
FIELDS = "kind,items(id,snippet(channelId,title,description,channelTitle))"

api_service_name = "youtube"
api_version = "v3"
DEVELOPER_KEY = "AIzaSyDQ_2nZTGkQN5YWLqQoHBpAvowFjIVjY8A"

youtube = googleapiclient.discovery.build(
	api_service_name , api_version , developerKey = DEVELOPER_KEY)


def index(request):
	regionData = get_regions()
	print("Getting the regions...")
	return render(request, 'base/index.html')

def get_regions():
  request = youtube.i18nRegions().list(
    part="snippet"
  )

  response = request.execute()
  response["items"].sort(key=lambda x: x['snippet']['gl'])

  return response
def get_channel_statistics(channelId):
	CHANNEL_ID = channelId

	#get channel statistics
	request = youtube.channels().list(
		part = "snippet,statistics",
		id = CHANNEL_ID,
		fields = "kind,items(kind,id,snippet(title,description),statistics)"
	)

	response = request.execute()

	#get channel videos
	request_videos = youtube.search().list(
		part = PART,
		channelId = CHANNEL_ID,
		maxResults = MAX_RESULTS,
		type = "video",
		fields = FIELDS
	)

	response_videos = request_videos.execute()

	final_data = {
		"channelData" : response,
		"videosData" : response_videos
	}

	return final_data

def searchResults(query_str, region_code):
	if query_str is not None:
		request = youtube.search().list(
			part = PART,
			maxResults = MAX_RESULTS,
			q = query_str,
			type = "video",
			fields = FIELDS,
			regionCode = region_code
		)
	response = request.execute()
	return response

def get_comments(id):
  request = youtube.commentThreads().list(
    part="snippet,replies",
    maxResults=MAX_RESULTS_COMMENTS,
    videoId=id
  )
  response = request.execute()

  return response

def buttonClick(request):
  query_str = request.POST.get("query_string")
  region_code = request.POST.get("region")
  print("Fetching Videos for the given string...")

  ## set default region code in case a user doesnot selects one
  if region_code == "":
    region_code = "US"

  search_list = get_search_list(query_str, region_code)
  regionData = get_regions()
  search_list = {"data": search_list, "regionData": regionData}

  return render(request,'searchPage.html',context=search_list)

def buttonClickStats(request):
	channelId = request.POST.get('statsButton')
