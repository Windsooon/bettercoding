function check(element) {
    if(element.$refs.answer_btn.getAttribute("val") == "0"){
        return false
    }
    else{
        return true
    }
}

function get_point() {
    if (!resource_div.seen) {
      console.log('right');
    }
}

function check_all() {
    answer_btn1.correct = check(answer_btn1);
    answer_btn2.correct = check(answer_btn2);
    answer_btn3.correct = check(answer_btn3);
    answer_btn4.correct = check(answer_btn4);
    resource_div.seen = true;
}

var answer_btn1 = new Vue({
  el: '#answer-1',
  data: {
    correct: false
  },
  methods: {
    check: function (event) {
        if(this.$refs.answer_btn.getAttribute("val") == "1") {
            get_point();
        }
        check_all()
    }
  }
})

var answer_btn2 = new Vue({
  el: '#answer-2',
  data: {
    correct: false
  },
  methods: {
    check: function (event) {
        if(this.$refs.answer_btn.getAttribute("val") == "1") {
            get_point();
        }
        check_all()
    }
  }
})

var answer_btn3 = new Vue({
  el: '#answer-3',
  data: {
    correct: false
  },
  methods: {
    check: function (event) {
        if(this.$refs.answer_btn.getAttribute("val") == "1") {
            get_point();
        }
        check_all()
    }
  }
})

var answer_btn4 = new Vue({
  el: '#answer-4',
  data: {
    correct: false
  },
  methods: {
    check: function (event) {
        if(this.$refs.answer_btn.getAttribute("val") == "1") {
            get_point();
        }
        check_all()
    }
  }
})

var resource_div = new Vue({
  el: '#resource-wrapper-div',
  data: {
    seen: false
  },
})
