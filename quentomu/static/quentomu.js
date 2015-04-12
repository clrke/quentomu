
angular.module('QuentomuApp', [])

.config(function($interpolateProvider, $httpProvider) {

	$interpolateProvider.startSymbol('{[');
	$interpolateProvider.endSymbol(']}');

	$httpProvider.defaults.xsrfCookieName = 'csrftoken';
	$httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
})

.controller('TopicsCtrl', ['$http', function ($http) {
	var Topic = this;
	$http.get('/topics').success(function (data) {
		Topic.values = data;
	})
}])

.controller('ConversationsCtrl', ['$http', '$interval',
		function ($http, $interval) {
	var Conversation = this;
	var refresh = function () {
		$http.get('/conversations').success(function (data) {
			replies = [];

			if(Conversation.values != null)
				Conversation.values.forEach(function (value) {
					if(value.reply != '') {
						replies.push({
							'friend': value.friend,
							'reply': value.reply
						});
					}
				});

			Conversation.values = data;

			replies.forEach(function (reply) {
				Conversation.values.forEach(function (conversation) {
					if(
						typeof conversation.friend == "string" ?
						conversation.friend == reply.friend :
						conversation.friend.id == reply.friend.id
					) {
						console.log(conversation.friend, reply.friend);
						conversation.reply = reply.reply;
					}
				})
			})
		});
	}
	refresh();

	Conversation.send = function (conversation) {
		if(conversation.reply == '') return;

		$http.post('/conversations', {
			"friend_id":
				typeof conversation.friend == "string" ?
					conversation.friend :
					conversation.friend.id,
			"reply": conversation.reply
		});

		conversation.messages.push({
			you: true,
			content: conversation.reply
		})
		conversation.reply = '';
	}

	Conversation.getFriendName = function (friend) {
		return typeof friend == "string" ? friend : friend.username
	}
}]);
