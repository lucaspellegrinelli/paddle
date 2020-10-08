import { shallowMount } from '@vue/test-utils';
import InformesLista from '../../src/views/InformesLista.vue';
import Informe from '../../src/components/Informe.vue';

jest.mock("axios", () => ({
    get: () => Promise.resolve({ data : {
                conteudo : [{id : '1', titulo : 'titulo1', data : 'data1', corpo: 'corpo1'},
                  {id : '2', titulo : 'titulo2', data : 'data2', corpo: 'corpo2'},
                  {id : '3', titulo : 'titulo3', data : 'data3', corpo: 'corpo3'},
                  {id : '4', titulo : 'titulo4', data : 'data4', corpo: 'corpo4'},
                  {id : '5', titulo : 'titulo5', data : 'data5', corpo: 'corpo5'},
                  {id : '6', titulo : 'titulo6', data : 'data6', corpo: 'corpo6'}]
                }})
  }))

describe('Testa InformesLista.vue', () => {
    
  it('Testa lista de posts', () => {
    var wrapper = shallowMount(InformesLista);

    //Testa se tem 6 posts em data
    wrapper.vm.$nextTick(() => {
      expect(wrapper.vm.posts.length).toBe(6);
    });  


    //Testa se o primeiro é o 1
    wrapper.vm.$nextTick(() => {
      informe_el = wrapper.findComponent(Informe);
      expect(informe_el.exists()).toBe(True);
      expect(informe_el.props('post_info')).toBe('corpo1');
    }); 
  });

  it('Testa paginação', () => {
    var wrapper = shallowMount(InformesLista);

    //Testa se tem 5 na página atual
    wrapper.vm.$nextTick(() => {
      expect(wrapper.findAllComponents(Informe)).toHaveLength(5);
    });  

    //Testa se os posts estão mudando corretamente ao mudar de página
    wrapper.setData({ pagina_atual: 2 })
    wrapper.vm.$nextTick(() => {
      informes = wrapper.findAllComponents(Informe);
      expect(informes).toHaveLength(1); //Testa se agora só tem 1 na página atual
      expect(informes.at(0).props('post_info')).toBe('corpo6'); //Testa se o primeiro é o 6
    });
  });

  it('Testa visibilidade do botão', () => {
    var wrapper = shallowMount(InformesLista);
  
    //Testa se botão de novo informe não existe
    expect(wrapper.find('.novo-informe').exists()).toBeFalsy()
  });
})