var output = $('.console-output');
var input = $("input[name='console-input']");
var DEFAULT_TIME = 30;
var timer_count = DEFAULT_TIME;
var key;

input.focus();

var timer = function() {
    if ( timer_count == 0 ) {
        clearInterval(interval);
        timer_count = DEFAULT_TIME;
        input.prop('disabled', false);
        
        output.html('Enter word:\n>>> ');
    }
    else {
        $('.remaining').html(timer_count);
        timer_count -= 1;
    }
};

var bashWrite = function(s, element) {
    var ssplit = s.split('\n');
    var cleared = false;
    
    for (var i = 0; i < ssplit.length; i++) {
        var line = ssplit[i];
        var esc = String.fromCharCode(0x1B);
        
        // Clear screen
        if (line.slice(0, 4) == esc + '[2J') {
            element.html('');
            cleared = true;
        }
        
        // End signal; disable input
        // This is a custom sequence
        else if (line.slice(0, 5) == esc + '[END') {
            input.prop('disabled', true);
        }
        
        // Start countdown
        // This is a custom sequence
        else if (line.slice(0, 6) == esc + '[CTDN') {
            do_countdown();
        }
        
        // Ignore (but don't print) all others
        else if (line[0] == esc);
        
        else {
            if (!i || (i > 0 && !cleared))
                element.append('\n');
                
            element.append(line);
            cleared = false;
        }
    }
};

var postToConsole = function(msg) {
    output.append(msg);
    
    $.post('http://adambeagle.com:8005', key + '\n' + msg, function(data) {
        var console = $('.console');
        
        bashWrite(data, output);
        console.scrollTop(console[0].scrollHeight);
    });
};

var start = function() {
    $.get('http://adambeagle.com:8005', function (data) {
        key = data.split('\n')[0];
        bashWrite(data.slice(key.length + 1, data.length), output);
    });
};

var do_countdown = function() {
    input.prop('disabled', true);
    output.append('\nYou have 30 seconds to determine your word.\n');
    setTimeout(function() { output.append('<span class="remaining"></span> seconds remaining...') }, 1000);
    interval = setInterval(timer, 1000);
};

// POST if enter is pressed while input box has focus
input.keypress(function(e) {
    if (e.which == 13) {
        var response = input.val();
        
        if (response) {
            postToConsole(response);
            input.val('');
        }
    }
});

$('.console').click(function() {
    input.focus();
});