<template>
	<div>
		<!-- <template v-for="(item, index) in items" :key="item.id"> -->
		<template v-for="(item, index) in evenItems" :key="item.id">
			<li>ID: {{ item.id }} 인덱스: {{ index }}, {{ item.message }}</li>
			<!-- <li v-if="item.id % 2 === 0"> -->
		</template>

		<li v-for="(value, key, index) in myObject" :key="key">
			{{ key }} - {{ value }} - {{ index }}
		</li>
	</div>
</template>

<script>
import { computed, reactive } from 'vue';
export default {
	setup() {
		const items = reactive([
			{ id: 1, message: 'Java' },
			{ id: 2, message: 'HTML' },
			{ id: 3, message: 'CSS' },
			{ id: 4, message: 'JavaScript' },
		]);

		const evenItems = computed(() => items.filter(item => item.id % 2 === 0));

		const myObject = reactive({
			title: '제목입니다.',
			author: '홍길동',
			publishedAt: '2016-04-10',
		});
		return { items, evenItems };
	},
};
</script>

<style lang="scss" scoped></style>
