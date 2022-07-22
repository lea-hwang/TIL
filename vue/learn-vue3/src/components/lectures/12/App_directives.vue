<template>
	<div>
		<!-- v-text: 내부 텍스트 값이 변할 때 사용 -->
		<p>{{ msg }}</p>
		<p v-text="msg"></p>
		<!-- v-html: html이 변할 때 사용 -->
		<p v-html="htmlStr"></p>
		<p v-text="htmlStr"></p>
		<!-- v-cloak: 로딩 될때까지만 있음 -->
		<div v-cloak>{{ message }}</div>
		<!-- v-once: 한번만 렌더링함. 업데이트 성능을 최적화하는데 사용할 수 있음 -->
		<p v-once>{{ msg }}!!!!</p>
	</div>
</template>

<script>
import { ref } from 'vue';
export default {
	setup() {
		const msg = ref('안녕하세요');
		const htmlStr = ref('<strong>안녕</strong>');
		const 
		return { msg, htmlStr };
	},
};
</script>

<style lang="scss" scoped></style>
