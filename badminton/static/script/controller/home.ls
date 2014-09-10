# home page

define [\jquery, \backbone], ($, Backbone) ->


  HomeView = Backbone.View.extend do
    el: \#main
    events:
      \click.btn : \_submit
    initialize: ->
      console.log \home_init
    _submit: ->
      alert \submit


