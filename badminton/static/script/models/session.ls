
define [
  \backbone
], (
  Backbone
) ->

  Session = Backbone.Model.extend do

    urlRoot: \session

    defaults:
      session_id: ""
      user_id: ""

    is-authorized: ->
      !!@session-id


