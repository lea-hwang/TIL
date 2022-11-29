<template>
	<div>
		<h2>{{ teacher.name }}</h2>
		<h3>강의가 있습니까?</h3>
		<p>{{ hasLecture }}</p>
		<p>{{ hasLecture }}</p>
		<p>{{ existLecture() }}</p>
		<p>{{ existLecture() }}</p>
		<button v-on:click="counter++">Counter: {{ counter }}</button>
		<h2>이름</h2>
		<p>{{ fullName }}</p>
	</div>
</template>

<script>
import { computed, reactive, ref } from 'vue';
export default {
	setup() {
		const teacher = reactive({
			name: '코딩',
			lectures: ['HTML/CSS', 'JavaScript', 'Vue3'],
		});

		const hasLecture = computed(() => {
			console.log('computed');
			return teacher.lectures.length > 0 ? '있음' : ' 없음';
		});

		const existLecture = () => {
			console.log('method');
			return teacher.lectures.length > 0 ? '있음' : ' 없음';
		};

		// computed: cached 데이터를 보관하고 있다가 해당 데이터를 돌려줌 그래서 computed는 한번만 실행됨.(실행되는 시점: 반응형 데이터가 변경되는 시점)
		// method: 실행될 때마다 실행됨

		const counter = ref(0);
		// method는 counter가 변할 때도 실행됨

		const firstName = ref('홍');
		const lastName = ref('길동');

		const fullName = computed({
			get() {
				return firstName.value + ' ' + lastName.value;
			},
			set(value) {
				console.log('value', value);
				console.log(value.split(' '));
				[firstName.value, lastName.value] = value.split(' ');
				// 구조분해할당을 통해 값 변경 -> firstName과 lastName의 값이 변경되었기 때문에 자동으로 getter 함수도 실행됨
				console.log('first: ', firstName.value);
				console.log('last: ', lastName.value);
			},
		});
		// computed는 기본적으로 할당이 불가능 하지만, getter와 setter를 따로 정의해줄 수 있음
		console.log('Console 출력:', fullName.value);
		fullName.value = '코딩 조아';
		return {
			teacher,
			hasLecture,
			existLecture,
			counter,
			firstName,
			fullName,
		};
	},
};
</script>

<style lang="scss" scoped></style>
