
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

.controller('ConversationsCtrl', ['$http', function ($http) {
	var Conversation = this;
	$http.get('/conversations').success(function (data) {
		Conversation.values = data;
	})

	Conversation.send = function (conversation) {
		if(conversation.reply == '') return;

		console.log($http.post);

		$http.post('/conversations', {
			"friend_id": conversation.friend.id,
			"reply": conversation.reply
		});

		conversation.messages.push({
			you: true,
			content: conversation.reply
		})
		conversation.reply = '';
	}
}]);
