<template>
	<div>
		<h1 v-if="visible">Hello Vue3</h1>
		<h1 v-else>false 입니다</h1>
		<button @click="visible = !visible">toggle</button>
		<hr />
		<button @click="type = 'A'">A</button>
		<button @click="type = 'B'">B</button>
		<button @click="type = 'C'">C</button>
		<button @click="type = 'D'">D</button>
		<h2 v-if="type === 'A'">A입니다</h2>
		<h2 v-else-if="type === 'B'">B입니다</h2>
		<h2 v-else-if="type === 'C'">C입니다</h2>
		<h2 v-else>A, B, C가 아닙니다</h2>
		<!-- 여러 태그를 하나로 묶어서 조건문을 적용하고 싶을 때, template을 사용 -->
		<template v-if="visible">
			<h1>Title</h1>
			<p>Paragraph 1</p>
			<p>Paragraph 2</p>
		</template>
		<!-- v-if는 렌더링이 되거나 안됨 -->
		<h1 v-show="show">Title</h1>
		<button @click="show = !show">toggle show</button>
		<!-- v-show는 렌더링은 되어있지만 display:none 처리됨 -->
		<!-- v-if는 전환비용이 높고 v-show는 초기 렌더링 비용이 높기 때문에 자주 변환해야한다면 v-show -->
	</div>
</template>

<script>
import { ref } from 'vue';
export default {
	setup() {
		const visible = ref(true);
		const type = ref('A');
		const show = ref(true);

		return { visible, type, show };
	},
};
</script>

<style lang="scss" scoped></style>
