<template>
	<div>
		<div :style="styleObject">
			Lorem, ipsum dolor sit amet consectetur adipisicing elit. A quae illum
			explicabo maiores quo dolore et debitis doloribus, ullam tempore, natus
			quos molestias quam molestiae voluptatibus esse laboriosam vel ducimus!
		</div>
		<button @click="fontSize++">+</button>
		<button @click="fontSize--">-</button>
	</div>
</template>

<script>
import { ref, computed } from 'vue';
export default {
	setup() {
		// const styleObject = reactive({
		// 	color: 'red',
		// 	fontSize: '13px',
		// });
		const fontSize = ref(13);

		const styleObject = computed(() => {
			return {
				color: 'red',
				fontSize: fontSize.value + 'px',
			};
		});
		return { styleObject, fontSize };
	},
};
</script>

<style lang="scss" scoped></style>
