import { shallowMount } from '@vue/test-utils';
import Home from '../../src/views/Home.vue';

describe('Testa Home.vue', () => {
    let wrapper;
    beforeEach(() => {wrapper = shallowMount(Home)});

    test('Testa botao do filtro', () => {
       //Checa se os botoes da pagina (filtrar e reset) sempre apareceme  funcionam
       wrapper.vm.$nextTick(() => {
           expect(wrapper.find('.informes').exists()).toBeTruthy();
           expect(wrapper.find('.rankings').exists()).toBeTruthy();
       }); 
    });

    test('Testa se os primeiros do ranking aparecem na tela inicial', () => {
        //Checa se aparecem os tres atletas mais bem classificados na tela inicial
        wrapper.vm.$nextTick(() => {
            expect(wrapper.vm.item1.lenght).toBe(1);
            expect(wrapper.vm.item2.lenght).toBe(1);
            expect(wrapper.vm.item3.lenght).toBe(1);
        });
    });

})
