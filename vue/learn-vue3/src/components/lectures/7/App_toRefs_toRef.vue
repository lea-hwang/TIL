<template>
	<div>
		<p>author: {{ author }}</p>
		<p>title: {{ title }}</p>
	</div>
</template>

<script>
import { reactive, toRefs, toRef } from '@vue/reactivity';
export default {
	setup() {
		const book = reactive({
			author: 'Vue Team',
			year; '2022',
			price: '무료',
			title: 'Vue 3 Guide'
		})

		// const { author, title } = book;
		console.log(typeof author) // string
		// 그냥 구조분해할당을 할 경우, 반응형을 잃어버림

		// const { author, title } = toRefs(book);
		// 구조분해할당을 하여도 반응형을 잃어버리지 않고 서로 동기화됨

		const author = toRef(book, 'author');
		const title = toRef(book, 'title');
		// 한가지씩 가져오고 싶을 때 사용

		return { author, title, book };
	},
};
</script>

<style lang="scss" scoped></style>
