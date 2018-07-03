Vue.component('skills-item', {
  props: ['skill'],
  template: `
    <div class="column skills-div">
      <p>{{ name }}</p>
    </div>
  `
})

var app = new Vue({ 
    delimiters: ['[[', ']]'],
    el: '#coding-title',
    data: {
      coding_title: 'Coding is more than algorithms.',
      seen: true,
      skills: [
        { id: 1, thumb: 1, name: 'My journey with Vue' },
        { id: 2, thumb: 2, name: 'Blogging with Vue' },
        { id: 3, thumb: 3, name: 'Why Vue is so fun' }
      ]
    },
    methods: {
      second: function () {
        this.seen = false
        this.coding_title = 'Choose your Favourite Topic.'
    }
  }
});
