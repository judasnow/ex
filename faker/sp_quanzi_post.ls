require! request
require! faker
require! config

faker.locale = "ja";

const CLIENT_ID = config.CLIENT_ID
const API_ROOT = \http://localhost:9000/1.1

const APIS =
  \auth : \/auth/access_token
  \new_topic : \/team/topics/new
  \reply_post : \/team/topics/reply

post-faker = ->
  {}

topic-faker = ->
  {
    title: faker.lorem.sentences!
    team_id: 1110
    content: faker.lorem.paragraph!
  } <<< post-faker!

# 执行 post 操作
post = (url, data, cb) !->
  request.post do
    url: url
    formData:
      {client_id: CLIENT_ID} <<< data
    (err, res, body) !->
      if err
        throw new Error err
      else
        cb res, body

# new topic
#post API.new_topic, topic-faker!, (res, body) ->
#  console.dir body


