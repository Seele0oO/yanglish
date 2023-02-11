<template>
  <div id="check-language">
    <div v-for="item in languages" :key="item.id">
      <input
        type="checkbox"
        :id="item.id"
        :value="item.value"
        v-model="item.selected"
        @change="checkLanguageSelectd(item.id)"
      />
      <label :for="item.id">{{ item.text }}</label>
    </div>
    <div>
      <button @click="getAllCheckd">获取所有选中的值</button>
    </div>
  </div>
</template>

<script>
export default {
  name: "APP",
  data() {
    return {
      // language: String,
      selectdLanguages: [],
      languages: [
        { id: 0, language: "zh", text: "中文", selected: false },
        { id: 1, language: "en", text: "英文", selected: false },
        { id: 2, language: "jp", text: "日语", selected: false },
        { id: 3, language: "ru", text: "俄语", selected: false },
        { id: 4, language: "fr", text: "法语", selected: false },
        { id: 5, language: "de", text: "德语", selected: false },
        { id: 6, language: "es", text: "西班牙语", selected: false },
      ],
    };
  },
  methods: {
    checkLanguageSelectd(id) {
      console.log(id);
      console.log(this.languages[id].selected);
      this.selectdLanguages.push(this.language);
    },

    getAllCheckd() {
      console.log(
        this.languages.filter((item) => item.selected)
        // this.languages.forEach((item) => {
        //   if (item.selected) {
        //     console.log(item.language);
        //   }
        // })
      );
    },
  },
};
</script>

<style>
.check-language {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  width: 100%;
  height: 100%;
}
</style>